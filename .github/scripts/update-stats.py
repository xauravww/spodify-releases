#!/usr/bin/env python3
"""Snapshot GitHub release download counts and refresh the README stats block.

GitHub exposes only a running total per asset, with no history: once a
download happens the number changes and yesterday's value is gone. Public
traffic stats are capped at a rolling 14-day window too. So this records one
data point per day into stats/downloads.json, which turns those totals into a
trend, and rewrites the block between the STATS markers in README.md.

Runs from .github/workflows/stats.yml once a day. Safe to re-run: a second run
on the same day overwrites that day's entry instead of appending a duplicate.

Usage:  python3 .github/scripts/update-stats.py [--dry-run]
"""

import datetime
import json
import os
import pathlib
import sys
import urllib.error
import urllib.request

REPO = "xauravww/spodify-releases"
ROOT = pathlib.Path(__file__).resolve().parents[2]
STATS_FILE = ROOT / "stats" / "downloads.json"
README = ROOT / "README.md"

START = "<!-- STATS:START -->"
END = "<!-- STATS:END -->"

# Don't keep an unbounded history file; two years of daily points is plenty and
# keeps the diff readable.
MAX_HISTORY = 730


def api(path: str):
    """GET a GitHub REST path, unauthenticated unless GITHUB_TOKEN is set."""
    req = urllib.request.Request(
        f"https://api.github.com/repos/{REPO}/{path}",
        headers={
            "Accept": "application/vnd.github+json",
            "User-Agent": "spodify-stats",
        },
    )
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(req, timeout=30) as res:
        return json.load(res)


def collect():
    """Current per-release download counts, newest release first."""
    releases = []
    for rel in api("releases?per_page=100"):
        if rel.get("draft"):
            continue
        releases.append(
            {
                "tag": rel["tag_name"],
                "published": (rel.get("published_at") or "")[:10],
                "downloads": sum(a.get("download_count", 0) for a in rel.get("assets", [])),
                "size": sum(a.get("size", 0) for a in rel.get("assets", [])),
                "prerelease": bool(rel.get("prerelease")),
            }
        )
    releases.sort(key=lambda r: r["published"], reverse=True)
    return releases


def load():
    if STATS_FILE.exists():
        try:
            return json.loads(STATS_FILE.read_text())
        except json.JSONDecodeError:
            pass
    return {"history": []}


def snapshot(state, releases):
    """Fold today's counts into the history, replacing a same-day entry."""
    today = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d")
    total = sum(r["downloads"] for r in releases)
    entry = {"date": today, "total": total}
    entry.update({r["tag"]: r["downloads"] for r in releases})

    history = [h for h in state.get("history", []) if h.get("date") != today]
    history.append(entry)
    history.sort(key=lambda h: h["date"])

    state["history"] = history[-MAX_HISTORY:]
    state["updated"] = datetime.datetime.now(datetime.timezone.utc).strftime(
        "%Y-%m-%dT%H:%M:%SZ"
    )
    state["total"] = total
    state["releases"] = releases
    return state, today


def delta(state, days):
    """Downloads added over the last N days, or None without enough history."""
    history = state["history"]
    if len(history) < 2:
        return None
    cutoff = (
        datetime.date.fromisoformat(history[-1]["date"]) - datetime.timedelta(days=days)
    ).isoformat()
    past = [h for h in history if h["date"] <= cutoff]
    if not past:
        return None
    return history[-1]["total"] - past[-1]["total"]


def render(state):
    releases = state["releases"]
    total = state["total"]
    lines = [
        START,
        "| Version | Published | Downloads | Share |",
        "| :--- | :--- | ---: | ---: |",
    ]
    for rel in releases:
        share = f"{rel['downloads'] / total * 100:.0f}%" if total else "—"
        label = f"**{rel['tag']}**" if rel is releases[0] else rel["tag"]
        lines.append(
            f"| {label} | {rel['published']} | {rel['downloads']} | {share} |"
        )
    lines.append(f"| **Total** | | **{total}** | |")

    trend = []
    for days, label in ((7, "last 7 days"), (30, "last 30 days")):
        value = delta(state, days)
        if value is not None:
            trend.append(f"{value:+d} in the {label}")
    summary = f"**{total} downloads** across {len(releases)} releases"
    if trend:
        summary += " · " + " · ".join(trend)
    lines.append("")
    lines.append(f"{summary} — updated {state['updated'][:10]}.")
    lines.append(END)
    return "\n".join(lines)


def write_readme(block, dry_run):
    text = README.read_text()
    if START not in text or END not in text:
        sys.exit(f"!! README is missing the {START} / {END} markers")
    head, rest = text.split(START, 1)
    _, tail = rest.split(END, 1)
    new = f"{head}{block}{tail}"
    if new == text:
        return False
    if not dry_run:
        README.write_text(new)
    return True


def main():
    dry_run = "--dry-run" in sys.argv
    releases = collect()
    state, _ = snapshot(load(), releases)
    changed_readme = write_readme(render(state), dry_run)

    if not dry_run:
        STATS_FILE.parent.mkdir(parents=True, exist_ok=True)
        STATS_FILE.write_text(json.dumps(state, indent=2) + "\n")

    print(f"total={state['total']} releases={len(releases)} readme_changed={changed_readme}")


if __name__ == "__main__":
    main()
