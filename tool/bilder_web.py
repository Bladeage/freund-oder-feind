"""Erzeugt aus den Quell-JPGs WebP-Varianten für die App (kleinere Downloads am Handy).

Aufruf (nach commons_fetch.py --apply):
    uv run python tool/bilder_web.py

Pro Asset entstehen assets/web/<id>-480.webp und -960.webp. Die JPGs bleiben die Quelle und
der Fallback. Bereits aktuelle Varianten werden übersprungen.
"""

import json
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
BREITEN = (480, 960)
QUALITAET = 80


def ziele(asset_id: str, root: Path = ROOT) -> list[Path]:
    return [root / f"assets/web/{asset_id}-{b}.webp" for b in BREITEN]


def main() -> None:
    eintraege = json.loads((ROOT / "assets/manifest.json").read_text())
    vorher = nachher = 0
    for e in eintraege:
        quelle = ROOT / e["datei"]
        vorher += quelle.stat().st_size
        with Image.open(quelle) as bild:
            bild = bild.convert("RGB")
            for breite, ziel in zip(BREITEN, ziele(e["id"]), strict=True):
                if not ziel.exists() or ziel.stat().st_mtime < quelle.stat().st_mtime:
                    ziel.parent.mkdir(parents=True, exist_ok=True)
                    hoehe = round(bild.height * breite / bild.width)
                    bild.resize((breite, hoehe), Image.LANCZOS).save(
                        ziel, "WEBP", quality=QUALITAET, method=6
                    )
                if breite == max(BREITEN):
                    nachher += ziel.stat().st_size
    print(f"{len(eintraege)} Assets: JPG {vorher / 1e6:.1f} MB -> WebP {nachher / 1e6:.1f} MB")


if __name__ == "__main__":
    main()
