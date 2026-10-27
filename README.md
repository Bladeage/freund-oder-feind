# Freund oder Feind

Lern-App zur Freund-Feind-Erkennung mit echten Bildern und Videos.
Swipe nach rechts für Freund, nach links für Feind.

Stand: Planung. Noch kein Feature-Code.

## Inhalt

| Pfad | Zweck |
|---|---|
| `docs/handover-2026-10-27.md` | Ziel, Entscheidungen, Quellen, Plan, offene Fragen. Eingabe für `/kickoff` |
| `docs/demo-v0/freund-oder-feind.html` | Demo aus Claude Web. Nur die Mechanik ist Vorlage, die Bilder nicht |
| `.claude/agents/bildpruefer.md` | Zweiter Agent: prüft Bilder und Videos |
| `.claude/agents/fachpruefer.md` | Zweiter Agent: prüft Merkmalstexte und Zuordnung |
| `.claude/agents/sichtpruefer.md` | Zweiter Agent: prüft Varianten und Sichten |

## Start in Claude Code

1. Ordner entpacken und im Terminal hineinwechseln.
2. `claude` starten.
3. Mit `/agents` prüfen, ob die drei Prüfer erscheinen.
4. `/kickoff docs/handover-2026-10-27.md` ausführen.
