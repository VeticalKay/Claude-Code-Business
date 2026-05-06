# Session Summary — 06.05.2026

## Thema
Buchhaltungs-Automatisierung: E-Mail-Rechnungen automatisch sortieren und speichern.

---

## Was wurde erledigt

### Skript `buchhaltung.py` (liegt auf dem Desktop)
- Python-Skript erstellt das automatisch Eingangsrechnungen (ER) und Ausgangsrechnungen (AR) aus E-Mails herauszieht
- Verbindet sich mit Tolkmit (`imap.tng.de`) und Verticalkay (`server1.codeking.at`)
- Erkennt Rechnungen anhand von Keywords (Rechnung, Invoice, Receipt etc.) + PDF-Anhang
- Speichert doppelt: **iCloud Drive** + **Google Drive**
- PayPal, Adobe, Apple → erstellt `.txt` Erinnerungsdatei mit direktem Link zum manuellen Download
- E-Mails nach Verarbeitung → ins **Archiv von Tolkmit** (`INBOX.Archive`) verschoben
- **Cron Job** eingerichtet: läuft täglich um 07:00 Uhr automatisch

### Ordnerstruktur (beide Pfade)
```
iCloud Drive/Dokumente/Katarina 2021/Steuererklärung/Steuererklärung 2026/
  ER/  → Januar, Februar, März, April, Mai ...
  AR/  → (Ausgangsrechnungen — noch nicht befüllt)

Google Drive/Meine Ablage/Steuererklärung/Steuererklärung 2026/
  ER/  → gleiche Struktur
  AR/  → gleiche Struktur
```

### Dateiname-Schema
```
2026-05-04_ER_Eversports_A-123456.pdf
2026-05-04_ER_PayPal_MANUELL-HERUNTERLADEN.txt
```

### Google Drive
- Desktop App installiert und eingerichtet (`katarina@tolkmit.de`)
- Pfad: `~/Library/CloudStorage/GoogleDrive-katarina@tolkmit.de/Meine Ablage/`

---

## Offene Punkte / Nächste Schritte

### Dringend
- [ ] **Richtigen iCloud-Pfad im Skript fixieren** — Katarina hat ER-Ordner manuell verschoben, Skript muss auf den exakten Pfad zeigen (Screenshot zu Beginn der nächsten Session zeigen)
- [ ] **Duplikate endgültig bereinigen** — in iCloud und Google Drive noch Dopplungen vorhanden, beim nächsten Mal mit frischem Blick sauber lösen
- [ ] **AR (Ausgangsrechnungen)** — Gesendet-Ordner Name für Tolkmit (`Gesendet` nicht gefunden) und Verticalkay (`Sent Messages` nicht gefunden) korrigieren

### Offen
- [ ] iCloud App-Passwort prüfen — war noch fehlerhaft, iCloud-Account läuft noch nicht
- [ ] Adobe als Erinnerungsdatei testen ob E-Mails erkannt werden
- [ ] Skript auf Digistore prüfen (Zahlungen via PayPal bereits abgedeckt)

---

## Wichtige Hinweise für nächste Session
- **processed.json NIE löschen** (`~/.buchhaltung_processed.json`) — verhindert Duplikate
- Skript prüft jetzt doppelt: processed.json UND ob Datei bereits existiert
- Beim Skript-Update: einfach neu ausführen, keine Duplikate
- Cron Job läuft bereits: `0 7 * * * /usr/bin/python3 ~/Desktop/buchhaltung.py`
