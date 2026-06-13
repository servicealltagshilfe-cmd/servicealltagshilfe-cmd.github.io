#!/usr/bin/env python3
"""
CarBro Icon-Generator
Erzeugt alle benötigten PNG-Icons (App, maskable, Apple-Touch, Favicon)
aus einem programmatisch gezeichneten Tacho-/Speedometer-Emblem.
Lauf:  python3 generate_icons.py
"""
import math
from PIL import Image, ImageDraw, ImageFilter

NAVY_TOP = (16, 27, 51)      # #101b33
NAVY_BOT = (3, 13, 37)       # #030d25
CYAN = (0, 218, 243)         # #00daf3
CYAN_LT = (156, 240, 255)    # #9cf0ff
GREEN = (169, 249, 0)        # neon accent


def vgradient(size, top, bot):
    """Vertikaler Farbverlauf."""
    img = Image.new("RGB", (size, size), top)
    px = img.load()
    for y in range(size):
        t = y / (size - 1)
        r = round(top[0] + (bot[0] - top[0]) * t)
        g = round(top[1] + (bot[1] - top[1]) * t)
        b = round(top[2] + (bot[2] - top[2]) * t)
        for x in range(size):
            px[x, y] = (r, g, b)
    return img


def rounded_mask(size, radius):
    m = Image.new("L", (size, size), 0)
    d = ImageDraw.Draw(m)
    d.rounded_rectangle([0, 0, size - 1, size - 1], radius=radius, fill=255)
    return m


def draw_emblem(size, full_bleed=False):
    """Tacho-Emblem auf transparentem RGBA-Layer (size x size), super-sampled."""
    S = size * 4  # supersample für glatte Kanten
    layer = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)

    cx, cy = S / 2, S / 2
    # Bei maskable (full_bleed) Motiv kleiner halten -> Safe-Zone
    scale = 0.30 if full_bleed else 0.34
    R = S * scale
    lw = int(S * 0.052)

    # Tacho-Bogen (offen unten), 150° bis 390°
    start, end = 150, 390
    bbox = [cx - R, cy - R, cx + R, cy + R]
    # dunkle Track
    d.arc(bbox, start, end, fill=(42, 52, 77, 255), width=lw)
    # cyan aktiver Bereich (ca. 70%)
    active_end = start + (end - start) * 0.72
    d.arc(bbox, start, active_end, fill=CYAN + (255,), width=lw)

    # Tick-Marks
    ticks = 9
    for i in range(ticks):
        a = math.radians(start + (end - start) * i / (ticks - 1))
        r1 = R - lw * 1.35
        r2 = R - lw * 2.25
        x1, y1 = cx + r1 * math.cos(a), cy + r1 * math.sin(a)
        x2, y2 = cx + r2 * math.cos(a), cy + r2 * math.sin(a)
        col = CYAN_LT if (start + (end - start) * i / (ticks - 1)) <= active_end else (130, 145, 160, 255)
        d.line([x1, y1, x2, y2], fill=col + (255,) if len(col) == 3 else col, width=int(S * 0.012))

    # Nadel (neon-grün), zeigt nach oben-rechts
    na = math.radians(start + (end - start) * 0.72)
    nx = cx + (R - lw * 0.7) * math.cos(na)
    ny = cy + (R - lw * 0.7) * math.sin(na)
    # Nadel als Dreieck
    perp = na + math.pi / 2
    bw = S * 0.022
    bx1 = cx + bw * math.cos(perp)
    by1 = cy + bw * math.sin(perp)
    bx2 = cx - bw * math.cos(perp)
    by2 = cy - bw * math.sin(perp)
    d.polygon([(nx, ny), (bx1, by1), (bx2, by2)], fill=GREEN + (255,))
    # Nabe
    hub = S * 0.055
    d.ellipse([cx - hub, cy - hub, cx + hub, cy + hub], fill=NAVY_BOT + (255,))
    d.ellipse([cx - hub, cy - hub, cx + hub, cy + hub], outline=CYAN + (255,), width=int(S * 0.012))

    # Downsample
    layer = layer.resize((size, size), Image.LANCZOS)
    # Glow
    glow = layer.filter(ImageFilter.GaussianBlur(size * 0.012))
    out = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    out = Image.alpha_composite(out, glow)
    out = Image.alpha_composite(out, layer)
    return out


def build(size, maskable=False):
    radius = 0 if maskable else int(size * 0.22)
    bg = vgradient(size, NAVY_TOP, NAVY_BOT).convert("RGBA")
    if not maskable:
        mask = rounded_mask(size, radius)
        bg.putalpha(mask)
    emblem = draw_emblem(size, full_bleed=maskable)
    bg = Image.alpha_composite(bg, emblem)
    return bg


def main():
    out = {
        "icon-192.png": (192, False),
        "icon-512.png": (512, False),
        "maskable-192.png": (192, True),
        "maskable-512.png": (512, True),
        "apple-touch-icon.png": (180, False),
        "favicon-32.png": (32, False),
    }
    for name, (sz, mask) in out.items():
        img = build(sz, maskable=mask)
        img.save(name)
        print("wrote", name, sz)
    # Play-Store 512 Hi-Res Icon (kein maskable, gefüllt)
    build(512, maskable=False).save("playstore-icon-512.png")
    print("wrote playstore-icon-512.png")


if __name__ == "__main__":
    main()
