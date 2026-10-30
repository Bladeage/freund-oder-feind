import json
from pathlib import Path

import pytest
from validate_manifest import FREI, ROOT, pruefe, pruefe_js

MANIFEST = ROOT / "assets/manifest.json"


def gueltig(tmp_path: Path) -> dict:
    (tmp_path / "assets").mkdir()
    (tmp_path / "assets/leo-seite-01.jpg").write_bytes(b"x")
    return {
        "id": "leo-seite-01",
        "fahrzeug": "Leopard 2A6",
        "untervariante": "",
        "kategorie": "fahrzeug",
        "seite": "freund",
        "nutzerstaat": "Deutschland",
        "ansicht": "seite",
        "typ": "bild",
        "datei": "assets/leo-seite-01.jpg",
        "quelle_url": "https://commons.wikimedia.org/wiki/File:X.jpg",
        "urheber": "Jemand",
        "lizenz": "CC BY 2.0",
        "lizenz_status": "geprueft",
        "aufnahme_datum": "2018-06-08",
        "aufnahme_ort": "",
        "kontext": "uebung",
        "stufe": "leicht",
        "spiegeln_erlaubt": False,
        "waermemaske": "",
        "variante_gesichert": False,
        "pruefbericht": "",
    }


def test_echtes_manifest_ist_gueltig():
    assert pruefe(json.loads(MANIFEST.read_text())) == []
    assert pruefe_js(MANIFEST) == []


def test_gueltiger_eintrag(tmp_path):
    assert pruefe([gueltig(tmp_path)], root=tmp_path) == []


@pytest.mark.parametrize(
    ("feld", "wert", "erwartet"),
    [
        ("seite", "partner", "seite="),
        ("kontext", "kino", "kontext="),
        ("stufe", "extrem", "stufe="),
        ("spiegeln_erlaubt", "nein", "true/false"),
        ("datei", "assets/fehlt.jpg", "Datei fehlt"),
        ("urheber", " ", "urheber leer"),
        ("nutzerstaat", "", "nutzerstaat leer"),
        ("quelle_url", "http://x", "https"),
        ("aufnahme_datum", "8.6.2018", "aufnahme_datum"),
        ("lizenz", "Copyrighted", "nicht frei"),
        ("pruefbericht", "docs/fehlt.md", "fehlende Datei"),
    ],
)
def test_fehler_werden_erkannt(tmp_path, feld, wert, erwartet):
    e = gueltig(tmp_path) | {feld: wert}
    fehler = pruefe([e], root=tmp_path)
    assert any(erwartet in f for f in fehler), fehler


def test_doppelte_id(tmp_path):
    e = gueltig(tmp_path)
    assert any("doppelt" in f for f in pruefe([e, dict(e)], root=tmp_path))


def test_release_verlangt_bericht_und_geprueft(tmp_path):
    e = gueltig(tmp_path) | {"lizenz_status": "unklar", "lizenz": "unbekannt"}
    fehler = pruefe([e], root=tmp_path, release=True)
    assert any("pruefbericht fehlt" in f for f in fehler)
    assert any("muss geprueft sein" in f for f in fehler)


@pytest.mark.parametrize(
    "lizenz", ["CC BY 2.0", "CC BY-SA 4.0", "CC BY-SA 3.0 de", "CC0", "Public domain"]
)
def test_freie_lizenzen(lizenz):
    assert FREI.match(lizenz)


@pytest.mark.parametrize("lizenz", ["CC BY-NC 4.0", "CC BY-ND 4.0", "Attribution", "PD-RU-exempt"])
def test_unfreie_oder_unscharfe_lizenzen(lizenz):
    assert not FREI.match(lizenz)
