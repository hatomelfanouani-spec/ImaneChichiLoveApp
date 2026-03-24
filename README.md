# 💖 Imane Chichi — Cinematic Love Story App

## 🎁 About
A premium, cinematic romantic PWA (Progressive Web App) — a private world of love, memories, music, and secret messages.

---

## 📱 How to Install on Android

### Method 1: Direct File (No Internet Required)
1. Copy the entire project folder to your Android device (via USB, WhatsApp, Google Drive, etc.)
2. Open **Chrome** on Android
3. Tap the address bar, type `file:///` and navigate to the `index.html` file
4. Chrome will show **"Add to Home Screen"** banner or tap ⋮ → **Add to Home Screen**
5. The app installs like a native app with its own icon! 🎉

### Method 2: Host Online (Recommended for Best Experience)
1. Upload all files to a free host:
   - **Netlify Drop**: drag folder to [app.netlify.com/drop](https://app.netlify.com/drop) — free, instant!
   - **GitHub Pages**: push to a public repo, enable Pages
   - **Vercel**: `npx vercel` in the folder
2. Open the URL in Chrome on Android
3. Tap ⋮ (three dots) → **Add to Home Screen**
4. Done! ✨

### Method 3: Using Local Server (Developer)
```bash
# Python
python3 -m http.server 8080

# Node.js
npx serve .

# Then open: http://localhost:8080
```

---

## 🔐 Default PIN
```
0 4 1 7
```
*(Imane's birthday: April 17th)*

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🔐 PIN Lock | Private access with custom 4-digit PIN |
| 🎬 Cinematic Hero | Full-screen animated intro with love counter |
| 🌳 Magic Love Tree | Interactive tree where fruits open sections |
| 💌 Love Letters | Write, save & delete private letters |
| 🎵 Song Player | Upload MP3s, play with audio visualizer |
| 💇 Hair Colors | Color picker with visual preview |
| 📸 Memory Gallery | Photo upload with fullscreen lightbox |
| 🌺 Love Quotes | 14 rotating romantic quotes |
| 🌙 Events Planner | Countdowns for Eid, Anniversary, Birthday |
| ✨ Dreams & Goals | Checklist with completion animations |
| 📜 Timeline | Animated story timeline from first meeting |
| 🔐 Secret Heart | Click 20 times to unlock hidden message |
| 🎮 Mini Game | Tap falling hearts — beat your high score! |
| 🎤 Voice Recorder | Record & play voice messages |
| 🗺️ Love Map | Save special places & memories |
| ⚙️ Settings | Theme colors, dark/light mode, volume, PIN |
| 💖 Particles | Floating hearts & stars background |
| 🎉 Confetti | Triggers on achievements & secrets |
| 📱 PWA | Installable, offline-capable app |

---

## 🎨 Customization

### Change the PIN
Open Settings (⚙️ icon) → Security → Change PIN

### Change Dates
In `index.html`, find these lines at the top of the script:
```javascript
const BIRTH_DATE = new Date('2003-04-17');  // Birthday
const FIRST_MEETING = new Date('2024-07-09'); // First meeting date
```

### Add Custom Quotes
Find `const LOVE_QUOTES = [` and add more entries:
```javascript
{ text: "Your quote here", author: "— Author" },
```

### Add Timeline Events
Find `const TIMELINE_EVENTS = [` and add:
```javascript
{ date: 'YYYY-MM-DD', title: 'Event Name 💕', desc: 'Description...' },
```

### Change Colors
In Settings → Theme Color, choose from 5 built-in palettes.
Or edit `const THEME_COLORS` in the script for custom colors.

---

## 📁 File Structure
```
imane-love-app/
├── index.html        ← Main app (entire app in one file)
├── manifest.json     ← PWA manifest
├── sw.js             ← Service Worker (offline support)
├── icons/
│   ├── icon-72.png
│   ├── icon-96.png
│   ├── icon-128.png
│   ├── icon-144.png
│   ├── icon-192.png
│   └── icon-512.png
└── README.md
```

---

## 💾 Data Storage
All data is saved locally in your browser's **localStorage**:
- Love letters
- Uploaded songs
- Photos
- Hair styles
- Dreams & goals
- Voice recordings
- Game high score
- Settings

**No data is ever sent anywhere** — this is 100% private.

> ⚠️ **Note**: Clearing browser data / cache will delete saved content.
> For important photos/songs, also keep originals elsewhere.

---

## 🚀 Optional Improvements
- Replace placeholder icons with a custom heart logo
- Add a real background music track (MP3 → base64 embed)
- Integrate Firebase for cloud backup
- Add real GPS coordinates to the Love Map
- Add push notifications for daily love messages
- Build as Android APK using TWA (Trusted Web Activity) via Bubblewrap CLI

---

## ❤️ Made with love
*Every line of this app was crafted with care for one special person.*

> *"You are my today and all of my tomorrows."*
