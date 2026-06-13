# Herzenssache – Beziehungsratgeber (E-Book)

Ein ehrlicher, praxisnaher Beziehungsratgeber für alle: Singles, Paare,
Verheiratete und jede Form der Liebe. Mit vielen Beispielen und konkreten
Tipps aus der Praxis.

## Dateien

- `build/Herzenssache.epub` – das fertige E-Book (EPUB, für alle gängigen
  Reader: Tolino, Kindle via Import, Apple Books, Google Play Books usw.)
- `build/cover.png` / `build/cover.jpg` – das Cover
- `content.py` – der gesamte Buchinhalt (18 Kapitel)
- `make_cover.py` – erzeugt das Cover
- `build_epub.py` – baut die EPUB-Datei

## Neu bauen

```bash
pip install ebooklib Pillow
cd ebook
python3 make_cover.py
python3 build_epub.py
```

## Inhalt (18 Kapitel)

Vorwort · Was Liebe wirklich ist · Warum wir lieben, wie wir lieben ·
Single sein · Partnersuche und Dating · Die Phasen einer Beziehung ·
Kommunikation · Streiten will gelernt sein · Vertrauen, Eifersucht und Treue ·
Nähe, Zärtlichkeit und Sexualität · Gleichgeschlechtliche und queere
Beziehungen · Verheiratet und Langzeitbeziehungen · Wenn es kriselt ·
Familie, Kinder und Patchwork · Geld, Alltag und das echte Leben ·
Trennung, Loslassen und Neuanfang · Selbstliebe · 50 Tipps zum Schluss
