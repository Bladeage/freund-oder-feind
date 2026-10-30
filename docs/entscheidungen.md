# Entscheidungen

Ergänzt bzw. ändert die Entscheidungen aus `handover-2026-10-27.md`. Neueste oben.

## 2026-10-30 · Ukrainisch genutzte Fahrzeuge zählen als Freund (Handover 10.1)
- **Entscheidung:** Freund = NATO-Staaten **und die Ukraine**. Feind = Russland und Belarus.
- **Maßgeblich ist der Nutzer auf dem Bild, nicht der Fahrzeugtyp.** Ein von der Ukraine genutzter
  (auch erbeuteter) T-72B3 ist eine Freund-Karte. Jedes Asset hat dafür `nutzerstaat`, und `seite`
  wird pro Asset gesetzt. Die App wertet nach dem Asset, nicht nach dem Typ.
- **Verworfen:** eigene Seite „Partner“ (mehr Umbau) und Ausschluss (verzichtet auf aktuelle Konfliktbilder).
- **Folge:** Solche Karten sind nur über Kennzeichen oder Lage lösbar. Sie sind bewusst Lehrkarten
  für „der Typ allein entscheidet nicht“.

## 2026-10-30 · Kontext „vorfuehrung“
Informationslehrübungen (ILÜ), Messen mit Fahrvorführung (z. B. Army-2016) und Tage der offenen Tür
zählen als `vorfuehrung`, nicht als `uebung`.

## 2026-10-30 · Öffentlicher PoC auf GitHub Pages
Das Repo ist öffentlich, `main` wird live ausgeliefert. Deshalb gehören Assets mit unklarer Lizenz
**nicht ins Repo**. Die CI erzwingt `validate_manifest.py --release`.
