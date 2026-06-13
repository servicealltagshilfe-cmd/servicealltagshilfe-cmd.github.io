#!/usr/bin/env python3
"""Erzeugt die Google-Play Feature-Grafik (1024x500) für CarBro."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "icons"))
from generate_icons import vgradient, draw_emblem, NAVY_TOP, NAVY_BOT, CYAN, GREEN
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 500
FONT = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
FONT_R = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"

def f(sz, bold=True):
    return ImageFont.truetype(FONT if bold else FONT_R, sz)

# Hintergrund: diagonaler Navy-Verlauf
bg = Image.new("RGB", (W, H), NAVY_TOP)
px = bg.load()
for y in range(H):
    for x in range(W):
        t = (x / W * 0.5 + y / H * 0.5)
        px[x, y] = (
            round(NAVY_TOP[0] + (NAVY_BOT[0] - NAVY_TOP[0]) * t),
            round(NAVY_TOP[1] + (NAVY_BOT[1] - NAVY_TOP[1]) * t),
            round(NAVY_TOP[2] + (NAVY_BOT[2] - NAVY_TOP[2]) * t),
        )
bg = bg.convert("RGBA")

# Emblem rechts
emb = draw_emblem(300, full_bleed=False)
bg.alpha_composite(emb, (W - 360, H // 2 - 150))

d = ImageDraw.Draw(bg)
# Marke
d.text((64, 150), "CarBro", font=f(96), fill=(255, 255, 255))
# Akzentlinie
d.rounded_rectangle([66, 258, 66 + 120, 266], radius=4, fill=CYAN)
# Tagline
d.text((64, 286), "Dein KFZ Starter Guide", font=f(40), fill=CYAN)
d.text((64, 344), "Auto kaufen · warten · verstehen –", font=f(28, False), fill=(186, 201, 204))
d.text((64, 382), "einfach erklärt für Anfänger.", font=f(28, False), fill=(186, 201, 204))

bg.convert("RGB").save(os.path.join(os.path.dirname(__file__), "feature-graphic-1024x500.png"))
print("wrote feature-graphic-1024x500.png")
