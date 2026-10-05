# 🎵 Spodify — The High-Fidelity Music Experience for Android

[![Latest Release](https://img.shields.io/github/v/release/xauravww/spodify-releases?color=1DB954&label=Latest%20Version&style=for-the-badge)](https://github.com/xauravww/spodify-releases/releases/latest)
[![Free](https://img.shields.io/badge/Price-100%25%20Free-1ED760?style=for-the-badge)](#-100-free-policy--scam-warning)
[![VirusTotal](https://img.shields.io/badge/VirusTotal-Clean%20(0%20Detections)-brightgreen?style=for-the-badge)](#-security--virustotal-verification)
[![Platform](https://img.shields.io/badge/Platform-Android%208.0%2B-blue?style=for-the-badge)](https://github.com/xauravww/spodify-releases/releases/latest)
[![License](https://img.shields.io/badge/Status-Actively%20Maintained-success?style=for-the-badge)](#-why-is-the-source-repository-private)

Spodify is an advanced, privacy-first Android music streaming client built with a native architecture. It delivers true **Studio Master 320 kbps** audio fidelity, multi-partner streaming failover, hardware DSP frequency tuning, real-time synchronized karaoke lyrics, and a built-in auto-updater — completely free of ads, subscriptions, and telemetry.

---

## 📥 Download Spodify

| Release | Version | Build | Package | Status |
| :--- | :--- | :--- | :--- | :--- |
| **Latest** | **v1.0.1** | 2 | `spodify-release.apk` | 🟢 Stable / Recommended |

👉 **[Direct Download: spodify-release.apk (v1.0.1)](https://github.com/xauravww/spodify-releases/releases/download/v1.0.1/spodify-release.apk)**

> 💡 **Seamless In-App Updates:** You only need to manually install the APK once. Every subsequent update is detected automatically by the built-in updater, allowing 1-tap downloads and installation directly inside the app.

---

## 📱 Visual App Tour

Below is a direct tour of Spodify's core interface, captured from live playback sessions.

| 🏠 Home & Discovery | ⚡ Streaming Partners | 📲 In-App Auto-Updater | 🎵 Now Playing & Artwork |
| :---: | :---: | :---: | :---: |
| <img src="screenshots/feature_home.png" width="220" alt="Home Screen" /> | <img src="screenshots/feature_streaming_partners.png" width="220" alt="Streaming Engine" /> | <img src="screenshots/feature_updater.png" width="220" alt="In-App Updater" /> | <img src="screenshots/feature_now_playing.png" width="220" alt="Now Playing Screen" /> |

| 🎤 Synchronized Lyrics | 🎚️ 10-Band Hardware DSP | 🌊 60 FPS Visualizer | 📋 Dynamic Queue |
| :---: | :---: | :---: | :---: |
| <img src="screenshots/feature_lyrics.png" width="220" alt="Synchronized Lyrics" /> | <img src="screenshots/feature_equalizer.png" width="220" alt="Hardware Equalizer" /> | <img src="screenshots/feature_visualizer_settings.png" width="220" alt="Audio Visualizer" /> | <img src="screenshots/feature_queue.png" width="220" alt="Queue Management" /> |

| 🔍 Universal Search | 🔄 Spotify Sync & Import | 📚 Your Library | 💾 Permanent Downloads |
| :---: | :---: | :---: | :---: |
| <img src="screenshots/feature_search.png" width="220" alt="Search Screen" /> | <img src="screenshots/feature_spotify_sync.png" width="220" alt="Spotify Sync" /> | <img src="screenshots/feature_library.png" width="220" alt="User Library" /> | <img src="screenshots/feature_downloads.png" width="220" alt="Offline Downloads" /> |

---

## 🚀 In-Depth Feature Breakdown

### 1. 🎧 Studio Master Streaming & Multi-Partner Engine
- **User-Selectable Engine**: Configure your prioritized streaming source under **Settings → Preferred Streaming Partner**:
  - **Studio Master (320 kbps)**: Highest fidelity progressive stream. Delivers rich dynamic range, uncompressed acoustic depth, punchy sub-bass, and crystal-clear high frequencies.
  - **Spotify Match**: 1:1 catalog matching based directly on Spotify track metadata, bypassing trackers and regional restrictions.
  - **Universal Catalog**: Maximum catalog coverage with 100M+ songs, covers, Indian regional music, and live performances.
- **Smart Failover Guarantee**: If a mirror encounters network latency, slow CDN response, or a missing regional track, Spodify's engine transparently fails over to the next mirror within milliseconds. You will never experience a stalled buffer or silence.
- **Permanent 56s/60s Cutoff Resolution**: Unlike naive streaming bots that stall at 56s due to chunk rate limits, Spodify incorporates progressive chunk streaming with zero cutoff timeouts.
- **100% Zero-Cookie Architecture**: No browser extensions, no cookie exports, and no expiring tokens. High-bitrate streaming works out of the box.

### 2. 🎚️ 10-Band Hardware DSP Equalizer
- **Direct Hardware Signal Processing**: Connects directly to Android's low-level audio output engine for latency-free real-time acoustic shaping.
- **10 Discrete Frequency Bands**: Fine-tune specific frequencies from deep sub-bass to air harmonics:
  `31 Hz` • `62 Hz` • `125 Hz` • `250 Hz` • `500 Hz` • `1 kHz` • `2 kHz` • `4 kHz` • `8 kHz` • `16 kHz` with ±12 dB precision control.
- **Bit-Perfect Audiophile Bypass Switch**: Enable pure direct output to disable all DSP processing and hear the untouched studio master recording.
- **Acoustic Presets**: Quick-switch presets for **Flat (Bit-Perfect)**, **Bass Booster**, **Acoustic**, **Vocal Enhancer**, and **Custom**.

### 3. 🎤 Real-Time Synchronized Karaoke Lyrics
- **Millisecond-Accurate Dynamic Lyrics**: Lyrics scroll dynamically with the artist's vocals in real time with high-visibility line tracking.
- **Interactive Tap-to-Seek**: Tap any lyric line (past or upcoming) to jump playback immediately to that exact timestamp.
- **Local Lyric Caching**: Once fetched, lyrics are saved locally for instant retrieval during offline or repeat listening.

### 4. 🌊 60 FPS Real-Time Audio Visualizer
- **Fluid Waveform Synthesis**: Renders smooth audio visualizers directly above playback controls with zero frame drops.
- **Multiple Visual Styles**:
  - **Equalizer Bars**: Classic multi-channel frequency spectrum bars.
  - **Neon Waveform**: Liquid oscillating neon wave.
  - **Radial Pulse**: Dynamic expanding acoustic pulse.
  - **Peak Spectrum**: High-contrast audio energy visualizer.
- **Color Accents**: Choose from Spotify Neon Green, Cyberpunk Amber, Electric Violet, or Neon Cyan.

### 5. 🔍 Universal Search & Discovery Explorer
- **Real-Time Query Completion**: Fast predictive search across tracks, artists, albums, and playlists.
- **Genre & Mood Explorer**: Dedicated visual tiles for Bollywood, Punjabi, Hip-Hop, Pop, Indie, Chill, Rock, and Workout.
- **Search Memory**: Quick-access chip shortcuts to re-run recent search queries instantly.

### 6. 🔄 Spotify Sync & Direct URL Importer
- **1-Tap URL Importer**: Paste any public Spotify playlist, track, or album link (`open.spotify.com/...`) to instantly resolve and match all songs with lossless audio.
- **Account Sync**: Sync your public or private Spotify playlists and liked tracks without requiring a Spotify Premium subscription or developer API credentials.

### 7. 💾 Permanent Offline Downloads
- **Zero Expiration**: Downloaded tracks are stored locally on your device with no time limits or periodic online check-in requirements.
- **Embedded Metadata & High-Res Art**: Downloads automatically embed ID3 tags, artist names, album titles, and high-resolution album covers.
- **Integrated Download Manager**: Manage downloaded storage, play entirely offline in Airplane mode, and shuffle downloaded libraries.

### 8. 📋 Live Session Queue & Continuous Radio
- **Up Next Management**: Review upcoming tracks, reorder positions, or swipe to remove songs from the active queue.
- **Infinite Radio Mode**: Spodify dynamically queues acoustically similar tracks once your selected playlist ends, ensuring non-stop music.

### 9. 📲 In-App Auto-Updater
- **Instant Version Discovery**: Automatically checks for new updates on launch using decentralized fallbacks.
- **Changelog Dialog**: Read detailed release notes and feature improvements before deciding to update.
- **1-Tap Direct Install**: Downloads the verified APK package directly within the app and triggers the native Android package installer. No Play Store or third-party stores needed.

---

## 🔒 Why is the Source Repository Private?

We believe in radical transparency with our community. The core codebase is currently hosted in a private repository for two critical reasons:

1. **Protecting Against Resellers & Predatory Rebranders:**  
   In the open-source audio community, bad actors frequently scrape free projects, remove the original developer's credits, slap ads on the code, and attempt to sell the APKs. Spodify was created for the community as a passion project and is **100% free forever** — keeping the core private ensures no scammer profits off our work.

2. **Long-Term Service Reliability & Infrastructure Stability:**  
   Exposing media routing pipelines, stream bypass techniques, and content delivery endpoints publicly invites scraper abuse, automated spam, and aggressive service provider lockouts. Maintaining the repository privately ensures Spodify stays fast, uninterrupted, and reliably functioning for all users over the long term.

> 🛠️ **Maintenance & Future:**  
> Spodify is actively maintained and updated by the developer. If future conditions allow for safe open-sourcing without risking community abuse or service takedowns, making the repository public will gladly be revisited.

---

## ⚠️ 100% Free Policy & Scam Warning

> ### 🛑 **NEVER PAY ANYONE FOR THIS APP!**
> **Spodify is completely free.**  
> If anyone attempts to sell you this app, charge for APK access, or ask for money/donations claiming to be associated with Spodify, **it is a scam**. Report them immediately.

---

## 🛡️ Security & VirusTotal Verification

Every official APK release is compiled from a clean source environment and scanned for security.

| Parameter | Details |
| :--- | :--- |
| **Package Name** | `com.spodify` |
| **Release File** | `spodify-release.apk` |
| **Version** | `v1.0.1` (Build 2) |
| **Target Architecture** | Universal Android (ARM64, ARMv7, x86_64) |
| **Minimum Android** | Android 8.0+ (Oreo) |
| **SHA-256 Checksum** | `e582f5a4ca0c6a9a18458038e642738a11a03e171b579912a14693b84e49b903` |
| **VirusTotal Report** | [🔍 View VirusTotal Scan Results](https://www.virustotal.com/gui/file/e582f5a4ca0c6a9a18458038e642738a11a03e171b579912a14693b84e49b903) **(0 Detections / 100% Clean)** |

### Checksum Verification
You can verify the integrity of the downloaded APK file in your terminal:
```bash
# Linux / macOS
sha256sum spodify-release.apk

# Windows PowerShell
Get-FileHash spodify-release.apk -Algorithm SHA256
```

---

## 🕵️ Privacy & Transparency

- **Zero Tracking & Analytics**: No analytics SDKs, no behavioral tracking, and no user profiling.
- **No Account Required**: Start listening immediately with zero login screens or email requirements.
- **Zero Personal Data Collected**: The developer does not collect, log, or have access to any user identity or personal data.
- **No Exploits**: Operates cleanly on-device utilizing public media standards. All settings and playlists remain entirely on your own device.

---

## 🐛 Bug Reports & Feature Requests

Encountered an issue or have an idea to make Spodify even better?  
Open a ticket on our official **[GitHub Issues](https://github.com/xauravww/spodify-releases/issues)** tracker!

When reporting an issue, please include:
- Your device model & Android version
- The song or action that triggered the issue
- Steps to reproduce

---

<p align="center">
  <b>Spodify</b> — Made with ❤️ for music enthusiasts everywhere.
</p>
