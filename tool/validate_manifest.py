"""Prüft das Asset-Manifest auf Schema, Dateien und Lizenzangaben.

Aufruf:
    python3 tool/validate_manifest.py              # Pilot-/Entwicklungsstand
    python3 tool/validate_manifest.py --release    # zusätzlich: Prüfbericht Pflicht, nichts unklar

Exit-Code 0 = gültig, 1 = Fehler gefunden.
"""

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

PFLICHT = [
    "id", "fahrzeug", "untervariante", "kategorie", "seite", "ansicht", "typ", "datei",
    "quelle_url", "urheber", "lizenz", "lizenz_status", "aufnahme_datum", "aufnahme_ort",
    "kontext", "stufe", "spiegeln_erlaubt", "waermemaske", "variante_gesichert", "pruefbericht",
]  # fmt: skip
WERTE = {
    "kategorie": {"fahrzeug", "tarnmuster", "kennzeichen"},
    "seite": {"freund", "feind"},
    "ansicht": {"seite", "front", "heck", "schraeg", "oben", "gelaende"},
    "typ": {"bild", "video"},
    "lizenz_status": {"geprueft", "unklar"},
    "kontext": {"uebung", "einsatz", "konflikt", "parade", "vorfuehrung", "museum"},
    "stufe": {"leicht", "mittel", "schwer"},
}
BOOL = ("spiegeln_erlaubt", "variante_gesichert")
ID = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)+$")
DATUM = re.compile(r"^(\d{4}(-\d{2}(-\d{2})?)?)?$")
# Lizenzen, die ohne Einzelfallprüfung weitergegeben werden dürfen.
# Portierte Fassungen (z. B. "CC BY-SA 3.0 de") sind ebenso frei.
FREI = re.compile(r"^(CC0( 1\.0)?|CC BY(-SA)? \d\.\d( [a-z]{2})?|Public domain)$")


def pruefe(eintraege: list[dict], root: Path = ROOT, release: bool = False) -> list[str]:
    fehler: list[str] = []
    ids: set[str] = set()
    for i, e in enumerate(eintraege):
        wo = e.get("id") or f"#{i}"
        f = lambda msg, wo=wo: fehler.append(f"{wo}: {msg}")  # noqa: E731

        for k in PFLICHT:
            if k not in e:
                f(f"Feld fehlt: {k}")
        for k, erlaubt in WERTE.items():
            if k in e and e[k] not in erlaubt:
                f(f"{k}={e[k]!r} nicht erlaubt")
        for k in BOOL:
            if k in e and not isinstance(e[k], bool):
                f(f"{k} muss true/false sein")

        if not ID.match(str(e.get("id", ""))):
            f("id muss kebab-case sein")
        if e.get("id") in ids:
            f("id doppelt")
        ids.add(e.get("id"))

        datei = e.get("datei", "")
        if datei and not (root / datei).is_file():
            f(f"Datei fehlt: {datei}")
        if datei and Path(datei).stem != e.get("id"):
            f("Dateiname passt nicht zur id")
        if not str(e.get("quelle_url", "")).startswith("https://"):
            f("quelle_url fehlt oder ist kein https")
        if not str(e.get("urheber", "")).strip():
            f("urheber leer")
        if not DATUM.match(str(e.get("aufnahme_datum", ""))):
            f("aufnahme_datum nicht im Format JJJJ[-MM[-TT]]")

        if e.get("lizenz_status") == "geprueft" and not FREI.match(str(e.get("lizenz", ""))):
            f(f"lizenz {e.get('lizenz')!r} ist nicht frei, lizenz_status muss unklar sein")
        for k in ("waermemaske", "pruefbericht"):
            if e.get(k) and not (root / e[k]).is_file():
                f(f"{k} verweist auf fehlende Datei: {e[k]}")

        if release:
            if e.get("lizenz_status") != "geprueft":
                f("Release: lizenz_status muss geprueft sein")
            if not e.get("pruefbericht"):
                f("Release: pruefbericht fehlt")
    return fehler


def pruefe_js(manifest: Path) -> list[str]:
    js = manifest.with_suffix(".js")
    if not js.is_file():
        return [f"{js.name} fehlt"]
    roh = js.read_text().strip()
    if not (roh.startswith("window.MANIFEST = ") and roh.endswith(";")):
        return [f"{js.name} hat unerwartetes Format"]
    if json.loads(roh[len("window.MANIFEST = ") : -1]) != json.loads(manifest.read_text()):
        return [f"{js.name} weicht von {manifest.name} ab (commons_fetch.py --apply neu laufen)"]
    return []


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--manifest", type=Path, default=ROOT / "assets/manifest.json")
    ap.add_argument("--release", action="store_true")
    a = ap.parse_args()

    eintraege = json.loads(a.manifest.read_text())
    fehler = pruefe(eintraege, release=a.release) + pruefe_js(a.manifest)
    for msg in fehler:
        print(f"FEHLER {msg}")
    print(f"{len(eintraege)} Einträge, {len(fehler)} Fehler")
    sys.exit(1 if fehler else 0)


if __name__ == "__main__":
    main()
