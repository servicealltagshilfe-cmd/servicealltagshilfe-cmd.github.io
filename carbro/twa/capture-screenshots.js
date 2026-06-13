/**
 * CarBro – Play-Store Screenshot-Generator
 * --------------------------------------------------
 * Erzeugt fertige Phone-Screenshots (1080 x 2340) für den Play-Store-Eintrag.
 * WICHTIG: Gegen die LIVE-URL laufen lassen, damit Icons/Fonts korrekt laden.
 *
 * Vorbereitung:
 *   npm install playwright
 *   npx playwright install chromium
 *
 * Ausführen (Standard-URL = GitHub Pages):
 *   node capture-screenshots.js
 * Eigene URL:
 *   BASE_URL=https://deine-domain.tld/carbro/ node capture-screenshots.js
 *
 * Ergebnis: store-assets/screenshots/01..06.png
 */
const fs = require("fs");
const path = require("path");
const { chromium } = require("playwright");

const BASE = process.env.BASE_URL || "https://servicealltagshilfe-cmd.github.io/carbro/";
const OUT = path.join(__dirname, "store-assets", "screenshots");

const SHOTS = [
  { hash: "home",        file: "01-home.png" },
  { hash: "kauf",        file: "02-kaufcheck.png" },
  { hash: "service",     file: "03-service.png" },
  { hash: "guide-reifen",file: "04-reifenwechsel.png" },
  { hash: "wissen",      file: "05-wissen.png" },
  { hash: "unfall",      file: "06-unfall.png" },
];

(async () => {
  fs.mkdirSync(OUT, { recursive: true });
  const browser = await chromium.launch();
  const page = await browser.newPage({
    viewport: { width: 1080, height: 2340 },
    deviceScaleFactor: 1,
    isMobile: true,
    hasTouch: true,
  });

  for (const s of SHOTS) {
    await page.goto(BASE + "#" + s.hash, { waitUntil: "networkidle" });
    // sicherstellen, dass die Icon-Font geladen ist
    await page.evaluate(() => document.fonts && document.fonts.ready);
    await page.waitForTimeout(800);
    await page.screenshot({ path: path.join(OUT, s.file) });
    console.log("✓", s.file);
  }

  await browser.close();
  console.log("\nFertig! Screenshots liegen in:", OUT);
})().catch((e) => { console.error(e); process.exit(1); });
