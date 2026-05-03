# Session Summary — 03.05.2026 (Abend)

## Was wurde besprochen
- Zeitkorrektur der Zoom-Meetings: Uhrzeit wurde falsch angezeigt (3:00 statt 15:00)
- Eversports-Integration: Zoom-Links einfügen + Kurse komplett anlegen (geplant für morgen)

## Was wurde erledigt

### Zoom Skript Timezone-Fix
- Ursache: Startzeit wurde ohne Wiener Zeitzone übergeben → Zoom zeigte falsche Uhrzeit an
- Skript korrigiert: `scripts/zoom_meetings_erstellen.py` gibt jetzt explizit `+02:00` (Sommer) bzw. `+01:00` (Winter) mit
- Katarina korrigiert die bereits erstellten Meetings manuell in Zoom

## Offene Punkte / Nächste Schritte

### Morgen (04.05.2026)
- **Eversports**: Zoom-Links in bestehende Kurse einfügen + neue Kurs-Termine anlegen
- Vorbereitung für morgen: Eversports Login (E-Mail + Passwort) + Kursliste (Name, Wochentag, Uhrzeit, Dauer, max. Teilnehmerinnen)
- Zoom-Meetings manuell auf 15:00–21:00 korrigieren
