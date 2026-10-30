# Prüfbericht Assets: pilot-01b (Nachtrag)

Prüfer: `bildpruefer` (unabhängiger Subagent), 2026-10-30. Geprüft wurden die neuen Assets `leo2a6-seite-02`, `leo2a6-front-02` und `pt91-seite-01` (heute `pt91-schraeg-02`) vollständig, bei den übrigen 8 nur die Felder. Vorbericht: `assets-pilot-01.md`.

Gesamturteil: nachbessern (ohne kritische und hohe Befunde)

Bei allen drei neuen Assets stimmen Typ, Seite und Lizenz. Es gibt keine Toten oder Verletzten, und `spiegeln_erlaubt: false` stimmt überall.

## Teil A – neue Assets
- **leo2a6-seite-02:** Leopard 2 ab A5 ist am Bild gesichert: Keilturm, 7 Laufrollen, Balkenkreuz. 2A6 gegen 2A5 ist am Bild nicht feststellbar, Rohrlänge im Mündungsfeuer. Freund gesichert. CC BY 2.0 (Flickr, Bundeswehr-Fotos), Rechtevermerk „©Bundeswehr/Langner“. Qualität gut.
- **leo2a6-front-02:** Leopard 2 mit Keilturm, Nahaufnahme der Wannenfront. Die Variante ist am Bild nicht feststellbar. Freund ist gesichert: Kennzeichen „Y-810 918“, Flecktarn. CC BY-SA 3.0 DE. Aufgenommen am Tag der offenen Tür, Marinestützpunkt Rostock Hohe Düne, 10.08.2024. Nur ein Ausschnitt, die Silhouette fehlt.
- **pt91-seite-01:** PT-91, gesichert durch das Nebelwerferbündel und die Quelle (15. Mech. Brigade, Saber Strike 18). Der Nutzerstaat ist am Bild nicht feststellbar. Gemeinfrei (US Army, Spc. Delany). Die Ansicht ist front-schräg, keine Seitenansicht.

## Befunde
| Schwere | Asset-ID | Problem | Vorschlag |
|---|---|---|---|
| mittel | pt91-seite-01 | `ansicht: seite` ist falsch, das Bild zeigt fast frontal. Es gibt keine echte PT-91-Seitenansicht. | `schraeg`/`front`, ID umbenennen, Seitenansicht nachbeschaffen |
| mittel | leo2a6-front-02 | `kontext: uebung` ist falsch, das Bild stammt vom Tag der offenen Tür. | `vorfuehrung` |
| mittel | leo2a6-seite-02 | `namensnennung` ist leer, obwohl die Quelle den Rechtevermerk „©Bundeswehr/Langner“ trägt. | `Bundeswehr/Langner` |
| mittel | BY-SA-Assets; alle CC-Assets | BY-SA: Varianten müssen wieder unter BY-SA stehen. Alle CC-Lizenzen verlangen, dass Änderungen kenntlich gemacht werden. | Auf der Bildnachweis-Seite „verändert“ vermerken und die BY-SA-Lizenz der Varianten nennen |
| niedrig | leo2a6-front-02 | `stufe: mittel` ist zu leicht, weil nur ein Ausschnitt zu sehen ist. | `schwer` |
| niedrig | pt91-seite-01 | `stufe: leicht` ist fraglich: Doppelnutzer, Staub. | `mittel` |
| niedrig | pt91-seite-01 | Der Nutzerstaat ist nur über die Quelle belegt. | hinnehmbar |
| niedrig | leo2a6-seite-02 | `aufnahme_ort` fehlt. | `Munster` |
| niedrig | leo2a6-seite-02, leo2a6-schraeg-02 | Eine ILÜ ist eine Vorführung. Die Kennzeichnung ist uneinheitlich, t72b3-silhouette-01 steht auf `vorfuehrung`. | ILÜ einheitlich als `vorfuehrung` |
| niedrig | pt91-seite-01 | Datum 2018-06-05 statt 2018-06-06 (Zeitzonen-Artefakt) | `2018-06-06` |
| niedrig | pt91-front-02 | Datum 2018-06-14 statt 2018-06-15 | `2018-06-15` |
| niedrig | leo2a6-schraeg-02 | Datum 2012-09-27 ist das Flickr-Datum, Aufnahme laut Beschreibung am 24.09. | `2012-09-24` |

## Teil B – Felder der übrigen Assets
Ohne Befund: leo2a6-schraeg-01 (Namensnennung erfüllt CC BY-SA 4.0), t72b3-schraeg-01 (`variante_gesichert: true` vertretbar: Gitter am Heck, Schürzen mit Klappsegmenten, Kategorie mod. 2016), t72b3-gelaende-01 (Namensnennung erfüllt die Mil.ru-Vorlage), t72b3-silhouette-01, pt91-front-02, pt91-gelaende-01, pt91-front-01 (Mehrfachlizenz GFDL/CC BY 3.0, Wahl von CC BY 3.0 zulässig).

## Umsetzung (2026-10-30, Branch `pruefung-pilot-01`)
| Befund | Status |
|---|---|
| pt91-seite-01 Ansicht | behoben: umbenannt in `pt91-schraeg-02`, `ansicht: schraeg`. **Offen:** echte PT-91-Seitenansicht nachbeschaffen. |
| leo2a6-front-02 Kontext, Stufe | behoben: `vorfuehrung`, `schwer` |
| leo2a6-seite-02 Namensnennung, Ort | behoben: `Bundeswehr/Langner`, `Munster` |
| ILÜ-Regel | behoben: ILÜ = `vorfuehrung` (leo2a6-seite-02, leo2a6-schraeg-02) |
| Daten | behoben: Spec kann `aufnahme_datum` vorgeben, drei Daten korrigiert |
| pt91 Stufe | behoben: `mittel` |
| ShareAlike / Änderungen kennzeichnen | **offen bis Phase 2:** Bisher zeigt die App die Bilder nur verkleinert, ohne Bearbeitung. Mit der Effekt-Engine kommt ein Hinweis „verändert“ in den Bildnachweis, bei BY-SA zusätzlich die Lizenz der Variante. |
