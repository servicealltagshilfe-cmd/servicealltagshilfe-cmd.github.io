# CarBro – Dein KFZ Starter Guide

Eine installierbare PWA (Progressive Web App), die Fahranfängern hilft, Autos zu
**kaufen, warten und zu verstehen**. Vorbereitet für die Veröffentlichung im
**Google Play Store** (als Trusted Web Activity).

**Live:** https://servicealltagshilfe-cmd.github.io/carbro/

## Features
- 🚗 **Kauf-Check** – interaktive Gebrauchtwagen-Checkliste mit Fortschritt
- 🔧 **Service-Guides** – Öl-Check, Reifenwechsel, Winter-Ready-Check
- 🚨 **Unfall-Guide** – Schritt-für-Schritt + Notruf 112
- 📚 **KFZ-Wissen** – komplexe Themen einfach erklärt, nach Kategorien filterbar
- 🎨 **Zwei Themes** – „Marine Cybernetic" & „Drive-Ready Tech" (umschaltbar)
- 💾 **Offline-fähig** & **lokale Speicherung** des Fortschritts (kein Konto, kein Tracking)

## Technik
- Reines HTML/CSS/JS, **keine Build-Tools nötig**, **keine externen Frameworks**
- Hash-basiertes SPA-Routing, `localStorage`-Persistenz, Service-Worker-Caching
- Checkbox-Häkchen in reinem CSS gezeichnet → funktioniert auch ohne geladene Icon-Font

## Lokal testen
```bash
# aus dem Repo-Root
python3 -m http.server 8099
# dann öffnen:  http://localhost:8099/carbro/
```

## Play-Store-Veröffentlichung
Siehe ausführliche Anleitung in **[PLAYSTORE.md](PLAYSTORE.md)**.

## Icons / Assets neu erzeugen
```bash
cd icons && python3 generate_icons.py          # App-Icons
cd ../twa/store-assets && python3 generate_feature.py   # Feature-Grafik
```

> ⚠️ CarBro ersetzt keine Fachwerkstatt, keinen Sachverständigen und keine
> Rechtsberatung. Alle Angaben ohne Gewähr.
