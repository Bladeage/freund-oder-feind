# Freund oder Feind

Lern-App zur Freund-Feind-Erkennung mit echten Bildern und Videos.
Swipe nach rechts für Freund, nach links für Feind.

Stand: Pilot. 3 Fahrzeuge (Leopard 2A6, T-72B3, PT-91 Twardy), 11 Fotos von Wikimedia Commons.
Bilder und Merkmalstexte sind unabhängig geprüft (`docs/pruefberichte/`). Noch keine Effekte/Sichten.

Live (PoC): https://bladeage.github.io/freund-oder-feind/ – jeder Merge auf `main` geht sofort online.

## Starten

`app/index.html` im Browser öffnen. Läuft ohne Server (auch per `file://`).
Mit `?unklar=1` werden auch Assets mit `lizenz_status: unklar` gezeigt (privater Build).

## Bilder holen

```sh
python3 tool/commons_fetch.py tool/pilot.json           # Dry-Run: Lizenz/Urheber anzeigen
python3 tool/commons_fetch.py tool/pilot.json --apply   # laden, Manifest schreiben
```

Nur Standardbibliothek. Lizenz und Urheber kommen aus der Commons-API, nicht aus der Spec.
Optional `COMMONS_KONTAKT` setzen (siehe `.env.example`) für den Wikimedia-User-Agent.

## Prüfen

```sh
uv sync                                          # Python 3.12, ruff, pytest
uv run pytest -q
uv run python tool/validate_manifest.py --release   # so prüft auch die CI
```

`--release` verlangt für jedes Asset `lizenz_status: geprueft` und einen Prüfbericht. Assets mit
unklarer Lizenz gehören **nicht ins Repo**, weil `main` öffentlich ausgeliefert wird.

Neue Assets und Texte durchlaufen die Prüf-Agenten (`bildpruefer`, `fachpruefer`), der Bericht kommt
nach `docs/pruefberichte/`, kritische und hohe Befunde werden vor dem Merge behoben.

## Inhalt

| Pfad | Zweck |
|---|---|
| `app/index.html` | Swipe-App (Mechanik aus Demo v0, echte Fotos, Bildnachweis pro Karte) |
| `assets/manifest.json` / `.js` | Asset-Manifest (Schema: Handover Abschnitt 8, erweitert um `untervariante`, `aufnahme_ort`, `stufe`, `namensnennung`); `.js` für `file://` |
| `assets/fahrzeuge/` | Fotos, 1280 px breit |
| `tool/commons_fetch.py` | Download + Metadaten von Wikimedia Commons |
| `tool/pilot.json` | Auswahl der Pilot-Fotos plus redaktionelle Felder (Ansicht, Stufe, Ort …) |
| `tool/validate_manifest.py` | Schema-, Datei- und Lizenzprüfung des Manifests |
| `docs/pruefberichte/` | Berichte der Prüf-Agenten mit Umsetzungsstand |
| `docs/handover-2026-10-27.md` | Ziel, Entscheidungen, Quellen, Plan, offene Fragen |
| `docs/demo-v0/freund-oder-feind.html` | Demo aus Claude Web. Nur die Mechanik ist Vorlage |
| `.claude/agents/` | Prüf-Agenten: `bildpruefer`, `fachpruefer`, `sichtpruefer` |
