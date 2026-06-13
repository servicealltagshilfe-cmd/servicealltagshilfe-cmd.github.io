#!/usr/bin/env python3
"""Erzeugt ein warmes, einladendes Cover fuer das Beziehungs-E-Book."""
import math
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H = 1600, 2400
OUT = "build/cover.png"

FONT_DIR = "/usr/share/fonts/truetype/liberation/"
FREE_DIR = "/usr/share/fonts/truetype/freefont/"


def font(path, size):
    return ImageFont.truetype(path, size)


def lerp(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))


# --- Hintergrund: warmer Sonnenuntergangs-Verlauf (oben rosa -> unten warmes Orange) ---
top = (255, 138, 128)     # warmes Korall-Rosa
mid = (255, 173, 122)     # Pfirsich
bot = (255, 209, 128)     # goldenes Gelb

bg = Image.new("RGB", (W, H), top)
px = bg.load()
for y in range(H):
    t = y / (H - 1)
    if t < 0.5:
        col = lerp(top, mid, t / 0.5)
    else:
        col = lerp(mid, bot, (t - 0.5) / 0.5)
    for x in range(W):
        px[x, y] = col

draw = ImageDraw.Draw(bg, "RGBA")

# --- weiche Lichtkreise (Bokeh) fuer Waerme ---
import random
random.seed(7)
for _ in range(26):
    r = random.randint(40, 150)
    cx = random.randint(0, W)
    cy = random.randint(0, H)
    a = random.randint(12, 38)
    layer = Image.new("RGBA", (r * 2, r * 2), (0, 0, 0, 0))
    ld = ImageDraw.Draw(layer)
    ld.ellipse([0, 0, r * 2, r * 2], fill=(255, 255, 255, a))
    layer = layer.filter(ImageFilter.GaussianBlur(r / 3))
    bg.paste(layer, (cx - r, cy - r), layer)

draw = ImageDraw.Draw(bg, "RGBA")


def heart(cx, cy, size, fill):
    """Zeichnet ein Herz mittig um (cx, cy)."""
    pts = []
    for deg in range(0, 360, 2):
        t = math.radians(deg)
        x = 16 * math.sin(t) ** 3
        y = 13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t)
        pts.append((cx + x * size, cy - y * size))
    draw.polygon(pts, fill=fill)


# --- zwei ineinander verschlungene Herzen (Verbindung / Liebe in allen Formen) ---
# weicher Schatten
shadow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
sd = ImageDraw.Draw(shadow)
def heart_on(d, cx, cy, size, fill):
    pts = []
    for deg in range(0, 360, 2):
        t = math.radians(deg)
        x = 16 * math.sin(t) ** 3
        y = 13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t)
        pts.append((cx + x * size, cy - y * size))
    d.polygon(pts, fill=fill)

cyc = 1000
heart_on(sd, 740, cyc + 18, 19, (120, 40, 40, 90))
heart_on(sd, 880, cyc + 18, 19, (120, 40, 40, 90))
shadow = shadow.filter(ImageFilter.GaussianBlur(14))
bg.paste(shadow, (0, 0), shadow)

draw = ImageDraw.Draw(bg, "RGBA")
# linkes Herz (kraeftiges Rot, halbtransparent), rechtes (warmes Weiss) -> Ueberlappung
heart(740, cyc, 19, (214, 51, 73, 235))
heart(880, cyc, 19, (255, 255, 255, 210))

# --- Titeltexte ---
serif_bold = font(FONT_DIR + "LiberationSerif-Bold.ttf", 150)
serif_it = font(FONT_DIR + "LiberationSerif-Italic.ttf", 64)
sans_reg = font(FONT_DIR + "LiberationSans-Regular.ttf", 46)
sans_bold = font(FONT_DIR + "LiberationSans-Bold.ttf", 40)


def centered(text, fnt, y, fill, shadow_col=(90, 30, 30, 110), dx=3, dy=3):
    bbox = draw.textbbox((0, 0), text, font=fnt)
    w = bbox[2] - bbox[0]
    x = (W - w) / 2 - bbox[0]
    if shadow_col:
        draw.text((x + dx, y + dy), text, font=fnt, fill=shadow_col)
    draw.text((x, y), text, font=fnt, fill=fill)


# kleine Vorzeile
centered("DER EHRLICHE BEZIEHUNGSRATGEBER", sans_bold, 150,
         (255, 255, 255, 235), shadow_col=(120, 50, 50, 120))
# dekorative Linie
draw.line([(W/2 - 230, 215), (W/2 + 230, 215)], fill=(255, 255, 255, 220), width=4)

# Haupttitel
centered("Herzenssache", serif_bold, 290, (255, 255, 255, 255))

# Untertitel (zwei Zeilen)
centered("Beziehungen verstehen,", serif_it, 480, (255, 252, 245, 255),
         shadow_col=(120, 50, 50, 90))
centered("leben und lieben", serif_it, 560, (255, 252, 245, 255),
         shadow_col=(120, 50, 50, 90))

# Zielgruppen-Zeile unten unter den Herzen
centered("Für Singles · Paare · Verheiratete · jede Liebe",
         sans_reg, cyc + 470, (255, 255, 255, 240),
         shadow_col=(120, 50, 50, 120))
centered("Mit vielen Beispielen und Tipps aus der Praxis",
         sans_reg, cyc + 540, (255, 255, 255, 235),
         shadow_col=(120, 50, 50, 120))

# Autorzeile ganz unten
centered("Ein Beziehungsratgeber von M. Zaebe", sans_bold, H - 180,
         (255, 255, 255, 240), shadow_col=(120, 50, 50, 120))

# feiner Rahmen
draw.rectangle([24, 24, W - 24, H - 24], outline=(255, 255, 255, 150), width=4)

bg.save(OUT, "PNG")
# zusaetzlich JPG fuer kleinere Dateigroesse im EPUB
bg.convert("RGB").save("build/cover.jpg", "JPEG", quality=88)
print("Cover gespeichert:", OUT)
