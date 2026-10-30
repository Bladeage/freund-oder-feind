# Prüfbericht Assets: pilot-01

Prüfer: `bildpruefer` (unabhängiger Subagent), 2026-10-30. Geprüfter Stand: Commit `b289afa`.
Umsetzung der Befunde: siehe Abschnitt „Umsetzung“ am Ende.

Gesamturteil: nachbessern

Kein kritischer und kein hoher Befund. Auf keinem Bild sind Tote oder Verletzte zu sehen. Es gibt keine Wasserzeichen oder Einblendungen, die Merkmale verdecken. Alle neun `quelle_url` wurden geöffnet. Lizenz und Urheber stimmen in allen neun Fällen formal mit der Commons-Seite überein. Nachzubessern sind vor allem drei Dinge: ein Lizenz-Restzweifel, die zu grobe Variantenangabe bei den T-72B3 und mehrere Werte für `ansicht` und `kontext`, die nicht passen.

## Befunde
| Schwere | Asset-ID | Problem | Beleg | Vorschlag |
|---|---|---|---|---|
| mittel | leo2a6-seite-01 | Die Gemeinfreiheit ist nicht voll belegt. Christoph Koppers ist kein Soldat. Laut Handover (Abschnitt 4) ist DVIDS nur für Material von US-Soldaten gesichert, alles andere ist pro Asset zu prüfen. | Auf DVIDS (Bild 4470638) steht als Einheit „Training Support Activity Europe“, als Credit „U.S. Army photo by Christoph Koppers“ und „Public Domain“. Ob er Bediensteter der US-Regierung ist, steht dort nicht. Bei einer deutschen Ortskraft wäre die Gemeinfreiheit nach 17 USC 105 strittig. | Nach der Regel „bei Zweifel unklar“: `lizenz_status: unklar`, bis sein Status belegt ist. |
| mittel | leo2a6-schraeg-01 | Ein Tarnnetz verdeckt fast alle Merkmale, die einen 2A6 ausmachen. Keil-Zusatzpanzerung an der Turmfront, Rohrlänge L/55 und Wannenbug sind nicht zu sehen. Am Bild ist nicht feststellbar, ob es ein 2A6, 2A5 oder 2A4 ist. | Sichtbar sind nur die Seitenschürzen, das Laufwerk mit 7 Laufrollen, die Mündung und die Turmdach-Silhouette. Die Variante ist nur durch die Quelle belegt. | Als schwere Karte für die Tarnung behalten, aber nicht als Grundbild für die 2A6-Merkmale. Ein unverdecktes Bild ergänzen. |
| mittel | t72b3-gelaende-01 | Der vordere Panzer ist stark mit Zweigen getarnt, die hinteren sind sehr klein. B3 und Modellstand sind am Bild nicht feststellbar. Den Nutzerstaat zeigt das Bild nicht: Laut Quelle verlegen hier Einheiten Russlands und von Belarus. | Commons-Beschreibung: „Выдвижение подразделений ВС РФ и Республики Беларусь…“. | Die Seite `feind` stimmt in jedem Fall. Als Gelände- oder Tarnkarte geeignet, nicht als Merkmalskarte. |
| mittel | alle t72b3-* | Das Feld `fahrzeug` lautet überall nur „T-72B3“. Laut Commons sind es verschiedene Modellstände: zweimal „mod. 2016“, einmal „mod. 2011“. | Commons-Kategorien | Den Modellstand erfassen, z. B. als Feld `untervariante`. |
| niedrig | t72b3-silhouette-01 | Die Qualität reicht nur für eine Silhouetten-Stufe: 900×600 px, Gegenlicht, Variante nicht feststellbar. | Commons-Original 900 × 600 px | Nur für schwere Karten. |
| niedrig | t72b3-silhouette-01 | `kontext: uebung` passt nicht genau. Laut Quelle ist es eine dynamische Vorführung auf dem Forum „Армия-2016“. | Commons: „динамический показ вооружения…“ | Mit `parade` kennzeichnen oder das Schema um `vorfuehrung` erweitern. |
| niedrig | leo2a6-front-01 | Eigentlich eine Schrägansicht, die linke Flanke ist voll sichtbar. | Bild | `ansicht: schraeg`. |
| niedrig | leo2a6-front-01 | Das Datum ist auf Commons widersprüchlich: 24.09. laut Beschreibung, 27.09.2012 laut EXIF. Variante: Keilturm der Familie 2A5/2A6/2A7, ein 2A7 ist vermutlich ausgeschlossen. 2A5 und 2A6 sind wegen der Verkürzung des Rohrs nicht zu trennen. | Commons-Dateiseite | Vermerken. |
| niedrig | pt91-schraeg-01 | Eigentlich nahezu frontal. | Bild | `ansicht: front`. |
| niedrig | pt91-schraeg-01 | Datum 14.06. laut Metadaten, 15.06.2018 laut Bildunterschrift. | Commons/DVIDS 4488164 | Vermerken. |
| niedrig | pt91-front-01 | Front-Schrägansicht, Grenzfall. | Bild | `front` kann bleiben. PT-91 hat damit keine Seitenansicht. |
| niedrig | leo2a6-schraeg-01, pt91-*, t72b3-silhouette-01 | Der Nutzerstaat ist am Bild nicht erkennbar und nur über die Quelle belegt. | Quellen | Die Seite stimmt jeweils. PT-91 wird seit 2022 auch in der Ukraine genutzt, das ist ein Hinweis für den Fachprüfer. |
| niedrig | leo2a6-schraeg-01 | Bei der Urheberangabe fehlt der Fotograf. | Commons: Fotograf Gerben van Es, Rechteinhaber Mediacentrum Defensie, CC BY-SA 4.0 | `Gerben van Es / Ministerie van Defensie`. Klären, ob die Varianten unter ShareAlike fallen. |
| niedrig | t72b3-gelaende-01, t72b3-silhouette-01 | Die mil.ru-Vorlage verlangt die Namensnennung „Mil.ru“. | Commons-Vorlage | „Mil.ru“ zusätzlich nennen. |
| niedrig | alle | Dem Manifest fehlt das Feld `aufnahme_ort` aus Handover Abschnitt 8. | Handover | Ergänzen. |

## Geprüft ohne Befund
- **t72b3-schraeg-01**, abgesehen vom Modellstand. Am Bild belegt: Kontakt-5-Keile an der Turmfront, Gitterschutz am Heck, Schürzen mit ERA-Modulen (mod. 2016). Russland ist am Bild gesichert: Moskau, Straßenschild, Paradestreifen. `variante_gesichert: true` wäre vertretbar.
- **pt91-gelaende-01**. ERAWA-Kacheln und Tellur-Werfer sind sichtbar.

Bei allen drei PT-91-Bildern ist der Typ am Bild an ERAWA und Tellur gesichert. Den Unterschied zum PT-91M (Malaysia) belegt nur die Quelle.

## Spiegeln pro Bild
| Asset-ID | Schrift/Markierung | `true` zulässig? |
|---|---|---|
| leo2a6-schraeg-01 | keine erkennbar | vermutlich ja, Originalauflösung prüfen |
| leo2a6-seite-01 | Balkenkreuze, Kennungen | nein |
| leo2a6-front-01 | Turmnummer „70“, Brückenklassenschild | nein |
| t72b3-schraeg-01 | kyrillische Schilder, Paradestreifen | nein |
| t72b3-gelaende-01 | keine erkennbar | vermutlich ja |
| t72b3-silhouette-01 | „Армия 2016“ | nein |
| pt91-schraeg-01 | Schilder | nein |
| pt91-gelaende-01 | oranges Schild | `false` vertretbar |
| pt91-front-01 | Turmnummer „8“ | nein |

Hinweis: Spiegeln vertauscht auch die Lage von Kommandant und Richtschütze (Sosna-U, Luken). Bewerten muss das der Sichtprüfer.

## Quellen
- https://commons.wikimedia.org/wiki/File:Leopard_2A6_Klietz_2018.jpg
- https://commons.wikimedia.org/wiki/File:German_Leopard_2a6_training_in_Germany_in_2018_-_180608-A-XV631-0107.jpg
- https://www.dvidshub.net/image/4470638/strong-europe-tank-challenge-2018-german-leopard-a6
- https://commons.wikimedia.org/wiki/File:Leopard_2A6_tank_-_IL%C3%9C_2012.jpg
- https://commons.wikimedia.org/wiki/File:T-72B3_(41072270245).jpg
- https://commons.wikimedia.org/wiki/File:T-72B3_mod._2016_at_the_Zapad-2017_exercise_03.jpg
- https://commons.wikimedia.org/wiki/File:Army-2016_(2016-09-06)_-_38.jpg
- https://commons.wikimedia.org/wiki/File:Polish_PT-91_Twardy_tank_Saber_Strike_18.jpg
- https://commons.wikimedia.org/wiki/File:PT-91_Twardy_during_exercise_Allied_Spirit_at_Bucierz_range,_Drawsko_Pomorskie_Training_Area,_Poland,_June_13,_2020_(3).jpg
- https://commons.wikimedia.org/wiki/File:POL_PT91_Twardy.jpg

## Umsetzung (2026-10-30, Branch `pruefung-pilot-01`)
| Befund | Status |
|---|---|
| leo2a6-seite-01 Lizenzzweifel | behoben: Asset entfernt, ersetzt durch `leo2a6-seite-02` (Bundeswehr, CC BY 2.0) |
| leo2a6-schraeg-01 Tarnnetz | behoben: `stufe: schwer`, zusätzlich unverdecktes Frontbild `leo2a6-front-02` |
| t72b3-gelaende-01 Eignung | behoben: `stufe: schwer` |
| T-72B3 Modellstand | behoben: neues Feld `untervariante` (mod. 2016 / mod. 2011); t72b3-schraeg-01 `variante_gesichert: true` |
| Silhouette Kontext | behoben: neuer Wert `vorfuehrung` |
| leo2a6-front-01 Ansicht | behoben: umbenannt in `leo2a6-schraeg-02` |
| pt91-schraeg-01 Ansicht | behoben: umbenannt in `pt91-front-02` |
| Klietz Fotograf, Mil.ru-Nennung | behoben: neues Feld `namensnennung`, wird im Bildnachweis angezeigt |
| `aufnahme_ort` fehlt | behoben: Feld ergänzt und befüllt |
| Datumswidersprüche | behoben, siehe Nachtrag `assets-pilot-01b.md` |
| ShareAlike bei Varianten | offen bis Phase 2 (Effekt-Engine) |

Die neuen Assets wurden im Nachtrag `assets-pilot-01b.md` geprüft.
