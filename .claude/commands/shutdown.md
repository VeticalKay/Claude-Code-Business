Fasse die aktuelle Session zusammen, speichere alle Änderungen und pushe alles auf GitHub.

1. Erstelle eine Session-Zusammenfassung in `outputs/` mit dem Dateinamen `YYYY-MM-DD-session-summary.md`:
   - Was wurde besprochen
   - Was wurde erledigt
   - Offene Punkte / nächste Schritte

2. Prüfe ob `context/current-data.md` aktualisiert werden muss (neue Erkenntnisse, geänderte Prioritäten).

3. Führe folgende Git-Befehle aus:
   - `git add context/ outputs/` — nur relevante Ordner stagen
   - `git commit -m "Session YYYY-MM-DD: [kurze Zusammenfassung was erarbeitet wurde]"`
   - `git push origin main`

4. Bestätige dem User:
   - Was committed und gepusht wurde
   - Den Link zum GitHub-Repository
   - Wichtige offene Punkte für die nächste Session
