"""Erzeugt Favicon, Homescreen-Icon und Teilen-Vorschau aus den Symbolen der App.

Aufruf (nur bei Designänderung nötig, Ergebnisse sind committet):
    uv run python tool/grafiken.py

Bewusst ohne Fahrzeugfoto: Eine Link-Vorschau zeigt keine Namensnennung, die CC-Lizenzen verlangen.
"""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
APP = ROOT / "app"
SCHRIFT = "/usr/share/fonts/liberation-sans-fonts/LiberationSans-{}.ttf"

OLIV, HELL, INK = "#2f3326", "#c9c8b4", "#23261c"
BLAU, ROT = "#80e0ff", "#ff8080"

SVG = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
<rect width="64" height="64" rx="12" fill="{OLIV}"/>
<rect x="7" y="21" width="22" height="22" rx="2" fill="{BLAU}" stroke="#000" stroke-width="2.5"/>
<rect x="38.5" y="22.5" width="19" height="19" fill="{ROT}" stroke="#000" stroke-width="2.5"
 transform="rotate(45 48 32)"/>
</svg>
"""


def symbole(d: ImageDraw.ImageDraw, x: float, y: float, g: float) -> None:
    """Freund-Quadrat und Feind-Raute nebeneinander, g = Kantenlänge."""
    rand = max(2, round(g / 9))
    d.rectangle([x, y, x + g, y + g], fill=BLAU, outline="#000", width=rand)
    cx, cy, r = x + g * 2.05, y + g / 2, g * 0.62
    d.polygon([(cx, cy - r), (cx + r, cy), (cx, cy + r), (cx - r, cy)], fill=ROT, outline="#000")
    d.line([(cx, cy - r), (cx + r, cy), (cx, cy + r), (cx - r, cy), (cx, cy - r)], "#000", rand)


def icon(groesse: int) -> Image.Image:
    bild = Image.new("RGB", (groesse, groesse), OLIV)
    g = groesse * 0.3
    breite = g * 2.67  # Quadrat + Abstand + Raute, siehe symbole()
    symbole(ImageDraw.Draw(bild), (groesse - breite) / 2, (groesse - g) / 2, g)
    return bild


def vorschau() -> Image.Image:
    bild = Image.new("RGB", (1200, 630), HELL)
    d = ImageDraw.Draw(bild)
    symbole(d, 90, 110, 120)
    d.text(
        (90, 290),
        "Freund oder Feind",
        font=ImageFont.truetype(SCHRIFT.format("Bold"), 104),
        fill=INK,
    )
    d.text(
        (92, 420),
        "Echte Fotos. Wischen. Merkmale lernen.",
        font=ImageFont.truetype(SCHRIFT.format("Regular"), 46),
        fill="#4b4e3f",
    )
    d.rectangle([0, 600, 1200, 630], fill=OLIV)
    return bild


def main() -> None:
    (APP / "icon.svg").write_text(SVG)
    icon(180).save(APP / "apple-touch-icon.png", optimize=True)
    vorschau().save(APP / "vorschau.png", optimize=True)
    print("app/icon.svg, app/apple-touch-icon.png, app/vorschau.png")


if __name__ == "__main__":
    main()
