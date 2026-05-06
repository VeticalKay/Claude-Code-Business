# Session Summary — 06.05.2026

---

# Session 1: Buchhaltungs-Automatisierung

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

## Offene Punkte

- [ ] **Richtigen iCloud-Pfad im Skript fixieren** — Katarina hat ER-Ordner manuell verschoben
- [ ] **AR (Ausgangsrechnungen)** — Gesendet-Ordner Name für Tolkmit & Verticalkay korrigieren
- [ ] iCloud App-Passwort prüfen
- [ ] Adobe als Erinnerungsdatei testen

## Wichtige Hinweise
- **processed.json NIE löschen** (`~/.buchhaltung_processed.json`) — verhindert Duplikate
- Cron Job läuft bereits: `0 7 * * * /usr/bin/python3 ~/Desktop/buchhaltung.py`

---

---

# Session 2: Ausbildungsskript Level 1.0 Basic Statictechnik

## Was besprochen wurde
Arbeit am **Ausbildungsskript Level 1.0 Basic Statictechnik** (Canva). Ziel: Inhaltsverzeichnis anpassen, Logo tauschen, Video-Links prüfen und fehlende Videos auflisten.

---

## Was erledigt wurde

### ✅ Skript identifiziert
- Canva-Design gefunden: **"Skript Level 1.0 Basic Statictechnik"**
- Design ID: `DAHDc3k9Loo` — 412 Seiten
- Edit-Link: https://www.canva.com/d/gAMQnlGVCEAI83v

### ✅ Backup-Kopie gesichert
- Katarina hat manuell eine Kopie erstellt
- Name: "Kopie von Skript Level 1.0 Basic Statictechnik"
- Design ID: `DAHIm_UmdwA`
- Liegt im Canva-Ordner: https://www.canva.com/folder/FAHIm_bK9Ds

### ✅ Video-Link Audit (vollständig)
- Alle 412 Seiten gescannt: **~45 Links vorhanden**, **14 fehlen**
- Gespeichert: `outputs/2026-05-04-skript-level1-static-videolinks.md`

**14 fehlende Videos:** Rauf rollen aus Kletterposition · Sichern im Klettern · Playleg Hold · Diamond Hold · Sichern Headstand Prep/Candle · Sichern Lean Back · Fehler Basic Walk · Push Turn VAR. B · Trucker Girl · Knee Bridge VAR. A+B · Basic Spin+Pencil Turn · Fan Kick+Basic Seat

### ✅ TOC-Analyse + Änderungsliste
- Befund: TOC bis Kap. 08 Slides ~2–3 Seiten zu hoch, ab Kap. 08 Seats ~50 Seiten zu hoch
- Ursache: 61 Seiten aus Original (500 Seiten) entfernt, TOC nie aktualisiert
- API-Limit: Canva erlaubt keine direkte Bearbeitung von 412-Seiten-Dokumenten
- Änderungsliste erstellt: `outputs/2026-05-06-toc-aenderungsliste-level1-static.md`

---

## Noch offen

- [ ] TOC manuell aktualisieren (Änderungsliste verwenden)
- [ ] ⚠️-Sub-Seiten beim Durchblättern selbst prüfen
- [ ] Logo tauschen (neues Logo als PNG bereitstellen)
- [ ] Fotos einfügen
- [ ] Beschreibungen mit Notizen anpassen
- [ ] 14 fehlende Videos aufnehmen + Links eintragen
