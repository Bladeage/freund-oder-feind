"""Lädt Bilder von Wikimedia Commons samt Lizenz-Metadaten und schreibt das Manifest.

Aufruf:
    python3 tool/commons_fetch.py tool/pilot.json            # Dry-Run: zeigt nur Metadaten
    python3 tool/commons_fetch.py tool/pilot.json --apply    # lädt Bilder, schreibt Manifest

Die Spec-Datei ist eine JSON-Liste mit Feldern des Manifests plus `commons_titel`.
Lizenz und Urheber kommen ausschließlich aus der Commons-API, nicht aus der Spec.
"""

import argparse
import html
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

from validate_manifest import FREI

API = "https://commons.wikimedia.org/w/api.php"
# Wikimedia verlangt einen aussagekräftigen User-Agent mit Kontakt; Kontakt über .env setzbar.
UA = f"FreundOderFeind/0.1 (Lern-App; {os.environ.get('COMMONS_KONTAKT', 'privat')})"
BREITE = 1280
PAUSE = 2.0
ROOT = Path(__file__).resolve().parent.parent


def get(url: str, versuche: int = 5) -> bytes:
    # Commons drosselt schnelle Folgeabrufe mit 429; Pause vor jedem Abruf, Retry mit Backoff.
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    for n in range(versuche):
        time.sleep(PAUSE)
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                return r.read()
        except urllib.error.HTTPError as e:
            if e.code != 429 or n == versuche - 1:
                raise
            time.sleep(int(e.headers.get("Retry-After") or 0) or 10 * (n + 1))
    raise AssertionError("unerreichbar")


def text(meta: dict, key: str) -> str:
    raw = meta.get(key, {}).get("value", "")
    return html.unescape(re.sub(r"<[^>]+>", "", str(raw))).strip()


def info(title: str) -> dict:
    q = urllib.parse.urlencode(
        {
            "action": "query",
            "titles": title,
            "prop": "imageinfo",
            "iiprop": "url|extmetadata|size|mime",
            "iiurlwidth": BREITE,
            "format": "json",
        }
    )
    page = next(iter(json.loads(get(f"{API}?{q}"))["query"]["pages"].values()))
    if "imageinfo" not in page:
        raise SystemExit(f"Nicht gefunden: {title}")
    return page["imageinfo"][0]


def eintrag(spec: dict) -> tuple[dict, str]:
    ii = info(spec["commons_titel"])
    meta = ii["extmetadata"]
    lizenz = text(meta, "LicenseShortName")
    e = {k: v for k, v in spec.items() if k != "commons_titel"}
    e.update(
        {
            "typ": "bild",
            "datei": f"assets/fahrzeuge/{spec['id']}.jpg",
            "quelle_url": ii["descriptionurl"],
            "urheber": text(meta, "Artist") or text(meta, "Credit"),
            "lizenz": lizenz,
            "lizenz_url": text(meta, "LicenseUrl"),
            "lizenz_status": "geprueft" if FREI.match(lizenz) else "unklar",
            # Spec darf das Datum vorgeben: Commons verschiebt DVIDS-Zeitstempel teils um einen Tag.
            "aufnahme_datum": spec.get("aufnahme_datum") or text(meta, "DateTimeOriginal")[:10],
            "pruefbericht": spec.get("pruefbericht", ""),
        }
    )
    return e, ii["thumburl"]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("spec", type=Path)
    ap.add_argument("--manifest", type=Path, default=ROOT / "assets/manifest.json")
    ap.add_argument("--apply", action="store_true")
    a = ap.parse_args()

    eintraege = []
    for spec in json.loads(a.spec.read_text()):
        e, thumb = eintrag(spec)
        print(f"{e['id']:<18} {e['lizenz']:<16} {e['lizenz_status']:<9} {e['urheber'][:40]}")
        if a.apply:
            ziel = ROOT / e["datei"]
            ziel.parent.mkdir(parents=True, exist_ok=True)
            ziel.write_bytes(get(thumb))
        eintraege.append(e)

    if not a.apply:
        print("\nDry-Run. Mit --apply laden und Manifest schreiben.", file=sys.stderr)
        return
    daten = json.dumps(eintraege, ensure_ascii=False, indent=2)
    a.manifest.write_text(daten + "\n")
    # Gleiche Daten als Skript, damit die App auch per file:// ohne fetch() läuft.
    a.manifest.with_suffix(".js").write_text(f"window.MANIFEST = {daten};\n")
    print(f"\n{len(eintraege)} Einträge -> {a.manifest.relative_to(ROOT)} (+ .js)")


if __name__ == "__main__":
    main()
