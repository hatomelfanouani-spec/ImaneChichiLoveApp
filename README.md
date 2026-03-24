# 💖 Imane Chichi — Cinematic Love Story App v2

> *A highly cinematic, romantic, fully customizable, interactive love story app*

---

## ✨ What's New in v2

- **6 color themes** + custom background images
- **Font selector** (Classic, Modern, Romantic)
- **Character photo** upload for the hair preview
- **Background music** upload + per-session playback
- **Voice recorder** with playback
- **Love Map** with date field
- **Custom events** (add your own countdowns)
- **Custom timeline** entries
- **Custom quotes** editor
- **Dream categories** with progress tracker
- **Data export/import** as JSON
- **Custom names** (change "Imane" and "You" to anything)
- **Achievement toasts** for every milestone
- **Confetti** on unlock + high score
- **Lightbox** with prev/next navigation

---

## 📱 How to Install on Android

### Method 1: Open File Directly (No Internet)
1. Copy the project folder to your Android device
2. Open **Chrome** on Android
3. Navigate to the `index.html` file (`file:///...`)
4. Tap ⋮ (three dots) → **Add to Home Screen**
5. Done! 🎉

### Method 2: Host Online (Best Experience — enables PWA fully)
1. Upload folder to **Netlify Drop**: drag to [app.netlify.com/drop](https://app.netlify.com/drop)
2. Open the given URL in Chrome on Android
3. Chrome will show "Add to Home Screen" banner
4. Or tap ⋮ → **Add to Home Screen**

### Method 3: Local Dev Server
```bash
python3 -m http.server 8080
# or
npx serve .
# then open http://localhost:8080
```

---

## 🤖 Build as Android APK (TWA)

### Using Bubblewrap (Google's official tool)

**Prerequisites:** Node.js 16+, Android Studio with SDK, Java 8+

```bash
# 1. Install Bubblewrap
npm install -g @bubblewrap/cli

# 2. Initialize TWA project (replace URL with your hosted URL)
mkdir imane-love-twa && cd imane-love-twa
bubblewrap init --manifest https://YOUR_HOSTED_URL/manifest.json

# 3. Configure when prompted:
#    - Package name: com.imanelove.app
#    - App name: Imane ♡
#    - Display: standalone
#    - Orientation: portrait

# 4. Build debug APK
bubblewrap build

# 5. Output: app-release-signed.apk
```

### Using PWA Builder (Easiest)
1. Host your app at a URL (Netlify free tier works)
2. Go to [pwabuilder.com](https://www.pwabuilder.com)
3. Enter your URL → click **Package for Stores**
4. Select **Android** → download APK/AAB

### Using Capacitor (Full Native)
```bash
npm install -g @capacitor/cli
npm init -y
npm install @capacitor/core @capacitor/android

# Initialize
npx cap init "Imane Love" com.imanelove.app --web-dir .

# Copy web files
npx cap add android

# Open in Android Studio
npx cap open android
```

Then in Android Studio: Build → Generate Signed Bundle / APK

---

## 🔐 Default PIN
```
0 4 1 7
```
*(Imane's birthday: April 17th)*
Change in: Settings → Security → Change PIN

---

## ✨ All Features

| Feature | Description |
|---------|-------------|
| 🔐 PIN Lock | 4-digit private access |
| 🎬 Cinematic Hero | Full-screen animated intro with love counter |
| 💌 Love Letters | Write, mood-tag & save private letters |
| 🎵 Songs | Upload MP3s with audio visualizer |
| 💇 Hair Colors | Color picker + photo face overlay |
| 📸 Gallery | Photo upload with lightbox + captions |
| 🌺 Quotes | 14 built-in + custom quotes editor |
| 🌙 Events | Countdowns + add custom events |
| ✨ Dreams | Checklist with categories & progress bar |
| 📜 Timeline | Story timeline + add your own events |
| 🔐 Secret Heart | Click 20× to unlock hidden message |
| 🎮 Mini Game | Tap falling hearts — beat your high score! |
| 🎤 Voice Recorder | Record & play voice messages |
| 🗺️ Love Map | Save special places with memories |
| ⚙️ Settings | Theme, fonts, BG, volume, PIN, names |
| 🎨 6 Themes | Rose, Rose Gold, Lavender, Emerald, Sunset, Ocean |
| 🖼️ Custom BG | Upload your own background image |
| 🔤 3 Fonts | Classic / Modern / Romantic |
| 💾 Export/Import | Backup all data as JSON |
| 🎉 Confetti | On achievements and unlocks |
| 💖 Particles | Floating hearts & sparkles |
| 📱 PWA | Installable, offline-capable |

---

## 🎨 Customization Guide

### Change Names
Settings → Personalization → Enter names → Save

### Change PIN
Settings → Security → Change PIN

### Change Theme Color
Settings → Appearance → Theme Color (6 options)

### Upload Background
Settings → Background → 📷 (last option)

### Add Custom Background Music
Settings → Audio → Upload BG Music → toggle on

### Edit Secret Message
Settings → Security → Edit Secret Message

### Add Custom Quotes
Quotes panel → scroll down → Add your own quote

### Add Timeline Events
Timeline panel → scroll down → Add a memory form

---

## 📁 File Structure
```
imane-love-app/
├── index.html          ← Complete app (self-contained)
├── manifest.json       ← PWA manifest
├── sw.js               ← Service Worker (offline)
├── icons/
│   ├── icon-72.png
│   ├── icon-96.png
│   ├── icon-128.png
│   ├── icon-144.png
│   ├── icon-192.png
│   └── icon-512.png
├── generate_icons.py   ← Icon generator script
└── README.md
```

---

## 💾 Data Storage
All data is stored in **localStorage** (your device only):
- Love letters, photos, songs, hair styles
- Dreams, timeline, events, voice recordings
- Settings, PIN, custom themes

**Zero data leaves your device** — 100% private.

> ⚠️ Clearing browser data will delete content.
> Use Settings → Export Data to back up regularly.

---

## ❤️ Made with love

*Every line crafted with care for one special person.*

> *"You are my today and all of my tomorrows."*
