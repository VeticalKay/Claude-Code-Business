# Session Summary — 06.05.2026 (Nachmittag)

## Thema
Google Drive API einrichten für remote Buchhaltungs-Automatisierung (ohne Mac).

---

## Was wurde erledigt

### Sicherheit
- E-Mail-Passwörter aus `buchhaltung.py` entfernt → jetzt sicher in `~/.config/buchhaltung/.env`
- Google Drive JSON-Schlüssel sicher in `~/.config/buchhaltung/` mit chmod 600
- `python-dotenv` installiert

### Google Cloud Console
- Google Drive API aktiviert (Projekt: My Maps Project, ferrous-pact-489614-h0)
- Dienstkonto "Buchhaltung" erstellt (Service Account — für später / Shared Drives)
- OAuth 2.0 Desktop-App "Buchhaltung" erstellt
- `katarina@tolkmit.de` als Testnutzer hinzugefügt
- OAuth Token einmalig autorisiert → gespeichert in `~/.config/buchhaltung/gdrive_token.json`

### Skript umgeschrieben
- `buchhaltung.py` jetzt mit Google Drive API (OAuth2 statt lokaler Pfad)
- Upload direkt in Google Drive Ordner "Steuererklärung" via API
- Kein Mac notwendig für den Upload
- Test erfolgreich: Upload + Delete Testdatei funktioniert ✅

### Ordner-Zustand
- iCloud: 41 PDFs, sauber, keine Duplikate ✅
- Google Drive: 41 PDFs, sauber, keine Duplikate ✅

---

## Dateien & Credentials

| Datei | Inhalt |
|-------|--------|
| `~/.config/buchhaltung/.env` | TOLKMIT_PASSWORD, VERTICALKAY_PASSWORD, GDRIVE_CREDENTIALS |
| `~/.config/buchhaltung/gdrive_credentials.json` | Service Account JSON (Backup) |
| `~/.config/buchhaltung/oauth_client.json` | OAuth2 Client Secret |
| `~/.config/buchhaltung/gdrive_token.json` | OAuth2 Token (automatisch erneuert) |
| `~/Desktop/buchhaltung.py` | Hauptskript |
| `~/Desktop/gdrive_auth.py` | Einmalige Auth (nicht mehr nötig) |

---

## Offene Punkte / Nächste Session

### Dringend
- [ ] **PythonAnywhere einrichten** (15-20 Min):
  1. Account erstellen auf pythonanywhere.com
  2. Skript + Credentials hochladen
  3. Tägliche Aufgabe (Scheduled Task) einrichten
  4. Token-Refresh auf PythonAnywhere lösen (anderes OS, kein Browser)

### Hinweis für PythonAnywhere
- Token wurde lokal erstellt — für PythonAnywhere brauchen wir entweder:
  - Den Token hochladen + Refresh Token nutzen (einfachste Lösung)
  - Oder: Token-Refresh-Logik ins Skript einbauen

### Noch offen (aus letzter Session)
- AR Gesendet-Ordner: `Gesendet` (Tolkmit) und `Sent Messages` (Verticalkay) nicht gefunden
- iCloud App-Passwort für iCloud IMAP (niedrige Priorität)

---

_Zuletzt aktualisiert: 06.05.2026_
