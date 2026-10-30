# Freund oder Feind

Lern-App zur Freund-Feind-Erkennung mit echten Bildern und Videos.
Swipe nach rechts für Freund, nach links für Feind.

Stand: Demo-Pilot. 3 Fahrzeuge (Leopard 2A6, T-72B3, PT-91 Twardy), je 3 Fotos von
Wikimedia Commons. Merkmalstexte noch ungeprüft, noch keine Effekte/Sichten.

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

## Inhalt

| Pfad | Zweck |
|---|---|
| `app/index.html` | Swipe-App (Mechanik aus Demo v0, echte Fotos, Bildnachweis pro Karte) |
| `assets/manifest.json` / `.js` | Asset-Manifest (Schema: Handover Abschnitt 8); `.js` für `file://` |
| `assets/fahrzeuge/` | Fotos, 1280 px breit |
| `tool/commons_fetch.py` | Download + Metadaten von Wikimedia Commons |
| `tool/pilot.json` | Auswahl der Pilot-Fotos |
| `docs/handover-2026-10-27.md` | Ziel, Entscheidungen, Quellen, Plan, offene Fragen |
| `docs/demo-v0/freund-oder-feind.html` | Demo aus Claude Web. Nur die Mechanik ist Vorlage |
| `.claude/agents/` | Prüf-Agenten: `bildpruefer`, `fachpruefer`, `sichtpruefer` |
