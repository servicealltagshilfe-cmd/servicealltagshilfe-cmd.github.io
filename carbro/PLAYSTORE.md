# 📲 CarBro im Google Play Store veröffentlichen

Diese Anleitung bringt **CarBro – Dein KFZ Starter Guide** Schritt für Schritt in den
Google Play Store. Die App ist eine **PWA** (im Ordner `/carbro/`), die als
**TWA** (Trusted Web Activity) verpackt wird – Google akzeptiert das als vollwertige
Android-App. Der Vorteil: Es gibt nur **eine Codebasis**. Jede Änderung an der Webseite
ist sofort auch in der App live (kein neues App-Update nötig, außer bei
Icon/Name/Version).

```
┌─────────────────────┐      verpackt als      ┌──────────────────────┐
│  PWA  /carbro/       │ ─────────────────────► │  TWA  (.aab)         │
│  (GitHub Pages)      │   Bubblewrap/PWABuilder│  → Google Play Store │
└─────────────────────┘                        └──────────────────────┘
        ▲                                                 │
        └──────── Digital Asset Links (assetlinks.json) ──┘
                  verbindet App ↔ Domain (entfernt die Browser-Leiste)
```

---

## ✅ Voraussetzungen

1. **Google Play Developer-Konto** – einmalig 25 USD: https://play.google.com/console/signup
2. **Web-App ist live** über HTTPS (siehe Schritt 1).
3. Für den lokalen Build (Methode B): **Node.js 18+** und **JDK 17+** (beides nur bei Bubblewrap nötig).

---

## Schritt 1 · Web-App live schalten (GitHub Pages)

Das Repository ist bereits ein GitHub-Pages-Repo (`servicealltagshilfe-cmd.github.io`).

1. Änderungen committen & pushen (ist nach diesem Task erledigt).
2. In GitHub: **Settings → Pages → Build and deployment → Source: „Deploy from a branch"**, Branch `main`, Ordner `/ (root)`.
3. Nach ein paar Minuten ist die App erreichbar unter:
   - **App:**  https://servicealltagshilfe-cmd.github.io/carbro/
   - **Manifest:**  https://servicealltagshilfe-cmd.github.io/carbro/manifest.webmanifest
   - **Asset-Links:**  https://servicealltagshilfe-cmd.github.io/.well-known/assetlinks.json
4. Kurz prüfen: App öffnet, Navigation, Checklisten haken ab, „Zur Startseite hinzufügen"
   wird angeboten (= PWA-Kriterien erfüllt). Optional mit Chrome DevTools → Lighthouse → PWA.

> ⚠️ GitHub Pages liefert `.well-known/`-Dateien aus (kein Sonderfall nötig). Die Datei
> `assetlinks.json` liegt bereits im Repo-Root unter `.well-known/`.

---

## Schritt 2 · Android-Paket (.aab) erzeugen

Es gibt zwei Wege. **Methode A ist am einfachsten** (nichts lokal installieren).

### 🅰️ Methode A — PWABuilder (empfohlen)

1. Auf **https://www.pwabuilder.com** die URL eingeben:
   `https://servicealltagshilfe-cmd.github.io/carbro/`
2. „Start" → PWABuilder analysiert die App → **„Package for stores"** → **Android**.
3. Einstellungen prüfen / setzen:
   - **Package ID:** `de.carbro.app`
   - **App name:** `CarBro – KFZ Starter Guide`
   - **Launcher name:** `CarBro`
   - **Theme/Background color:** `#08132a`
   - **Signing key:** „Create new" (PWABuilder erzeugt einen Upload-Key).
4. **„Generate"** → es wird ein ZIP heruntergeladen mit:
   - `*.aab`  → das lädst du in den Play Store hoch
   - `signing.keystore` + `signing-key-info.txt` → **GUT AUFBEWAHREN!** (Passwörter!)
   - `assetlinks.json` → enthält den korrekten SHA-256-Fingerprint
5. Weiter mit **Schritt 3**.

> 💡 PWABuilder liest automatisch `manifest.webmanifest`, Icons und Shortcuts ein –
> die sind in diesem Projekt bereits korrekt gesetzt.

### 🅱️ Methode B — Bubblewrap CLI (lokal, mehr Kontrolle)

Die fertige Konfiguration liegt unter `carbro/twa/twa-manifest.json`.

```bash
# 1) Bubblewrap installieren
npm install -g @bubblewrap/cli

# 2) In den TWA-Ordner wechseln
cd carbro/twa

# 3) Projekt aus der vorhandenen Manifest-Datei initialisieren
bubblewrap init --manifest ./twa-manifest.json
#    (beim ersten Mal lädt Bubblewrap JDK + Android-SDK automatisch herunter)

# 4) Signing-Key erstellen (einmalig) – Passwörter NOTIEREN!
keytool -genkeypair -v -keystore android.keystore -alias carbro \
        -keyalg RSA -keysize 2048 -validity 9125 -storetype JKS

# 5) Bauen
bubblewrap build
#    -> erzeugt  app-release-bundle.aab  (für den Store)
#    -> erzeugt  app-release-signed.apk  (zum lokalen Testen)
```

Fingerprint deines Keys ermitteln (für `assetlinks.json`, falls du **kein** Play App
Signing nutzt):
```bash
keytool -list -v -keystore android.keystore -alias carbro | grep SHA256
```

---

## Schritt 3 · Digital Asset Links setzen (Browser-Leiste entfernen)

Damit die App ohne Adressleiste im Vollbild läuft, muss die Domain die App
„bestätigen".

> 🚨 **Wichtigster & häufigster Fehler:** Wenn du **Play App Signing** nutzt (Standard,
> empfohlen), signiert **Google** die App neu. Dann zählt **nicht** der Fingerprint
> deines Upload-Keys, sondern der von Google!
> Den findest du nach dem ersten Upload in der **Play Console →
> Release → Setup → App-Integrität → „App-Signaturschlüssel-Zertifikat" → SHA-256**.

1. Den korrekten **SHA-256-Fingerprint** kopieren.
2. In `/.well-known/assetlinks.json` den Platzhalter ersetzen:
   ```json
   "sha256_cert_fingerprints": [
     "AB:CD:12:34:...:EF"   ← hier einfügen
   ]
   ```
   `package_name` muss `de.carbro.app` bleiben (bzw. deine gewählte Package-ID).
3. Committen & pushen → live unter
   `https://servicealltagshilfe-cmd.github.io/.well-known/assetlinks.json`.
4. Prüfen mit Googles Tester:
   `https://developers.google.com/digital-asset-links/tools/generator`

> Du kannst sowohl den Upload-Key- **als auch** den Google-Fingerprint eintragen
> (mehrere Einträge sind erlaubt) – dann funktioniert es in jedem Fall.

---

## Schritt 4 · In der Play Console veröffentlichen

1. **App erstellen** → Name `CarBro – KFZ Starter Guide`, Sprache Deutsch, „App", „Kostenlos".
2. **Store-Eintrag** ausfüllen → Texte & Grafiken aus
   `carbro/twa/store-assets/store-listing-de.md` und dem Ordner `store-assets/`:
   - App-Icon: `playstore-icon-512.png`
   - Feature-Grafik: `feature-graphic-1024x500.png`
   - Screenshots: mit `capture-screenshots.js` gegen die Live-URL erzeugen (siehe unten)
3. **Pflicht-Formulare** (linke Leiste, „App-Inhalte"):
   - **Datenschutzerklärung:** `https://servicealltagshilfe-cmd.github.io/carbro/datenschutz.html`
   - **Datensicherheit:** „Es werden keine Daten erhoben/geteilt" (siehe Listing-Datei)
   - **Inhaltseinstufung:** Fragebogen → USK 0 / PEGI 3
   - **Zielgruppe:** ab 13 Jahren (keine Kinder-App)
   - **Werbung:** „Enthält keine Werbung"
4. **Release erstellen:** zuerst **Internal testing** (schnell, nur du) →
   `.aab` hochladen → testen → dann **Production**.
5. **Einreichen.** Erstprüfung dauert i. d. R. einige Stunden bis wenige Tage.

### Screenshots erzeugen
```bash
cd carbro/twa
npm install playwright && npx playwright install chromium
node capture-screenshots.js          # nutzt die Live-URL automatisch
# -> store-assets/screenshots/01..06.png
```

---

## 🔄 Updates später

- **Inhalts-/Text-/Design-Änderung:** einfach Webseite ändern & pushen – sofort in der App
  live, **kein** Play-Update nötig.
- **Icon, App-Name, Berechtigungen, Version:** `appVersionCode` in `twa-manifest.json`
  erhöhen (z. B. 1 → 2), neu bauen, neues `.aab` in der Play Console hochladen.

---

## 📁 Dateiüberblick

```
carbro/
├── index.html              ← die App (Single-Page-PWA)
├── app.css                 ← Styles (2 Themes)
├── app.js                  ← Logik, Routing, Persistenz
├── manifest.webmanifest    ← PWA-Manifest (von TWA/PWABuilder gelesen)
├── sw.js                   ← Service-Worker (Offline)
├── offline.html            ← Offline-Fallback
├── datenschutz.html        ← Datenschutz (Play-Pflicht)
├── icons/                  ← App-Icons (any + maskable) + Generator
└── twa/
    ├── twa-manifest.json       ← Bubblewrap-Konfiguration
    ├── capture-screenshots.js  ← Store-Screenshots erzeugen
    └── store-assets/
        ├── store-listing-de.md       ← alle Store-Texte (Copy & Paste)
        ├── feature-graphic-1024x500.png
        ├── playstore-icon-512.png
        └── generate_feature.py
.well-known/
└── assetlinks.json         ← Digital Asset Links (Fingerprint eintragen!)
```

Viel Erfolg beim Launch! 🚀
