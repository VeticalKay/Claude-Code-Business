# Session Summary — 25. April 2026 (Session 2: Prüfungskalender)

## Was besprochen wurde

### Thema: Prüfungstermine-Tabelle & Online-Kalender

Katarina möchte ihre bestehende Google Sheets Tabelle für Prüfungstermine:
1. Bereinigen und strukturieren
2. Mit einer vollständigen Schülerinnenliste + Warteliste ergänzen
3. In einen Online-Kalender auf ihrer WordPress-Website umwandeln
4. Mit Google Drive Links der Schülerinnen verknüpfen (Prüfungsunterlagen direkt aus dem Kalender abrufbar)

---

## Analyse der bestehenden Tabelle

**Google Sheets ID:** `1swKRF_u9mDVsNXHOOZkVTwr5O6J3qCZwAxxWNol8GBI`

**Probleme der aktuellen Tabelle:**
- Mehrere inkonsistente Tabellenformate durcheinander
- Tippfehler in Datumsangaben (z.B. `11..09.26`)
- Tippfehler in Spaltenbezeichnungen (`Konrtolliert`, `Zertfikat`)
- Einträge teils ohne alle Spalten
- Warteliste als loses Textfeld, nicht strukturiert

**Gebuchte Zukunftstermine (rekonstruiert):**

| Datum | Zeit | Schülerin | Ausbildung |
|-------|------|-----------|------------|
| 01.05.26 | 11:00–13:00 | Manya Teil 2 | Basic Trainer |
| 08.05.26 | 13:30–15:30 | Lea Sophie Teil 1 | Basic Trainer |
| 14.05.26 | 12:00–14:00 | Andrea Herzog Teil 1 | Basic Trainer |
| 25.05.26 | 12:00–14:00 | Andrea Herzog Teil 2 | Basic Trainer |
| 12.06.26 | 13:30–15:30 | Anna ter Vehen Teil 1 | Basic Trainer |
| 20.06.26 | 11:00–13:00 | Andrea Herzog Teil 1 | Intermediate Trainer |
| 04.07.26 | 11:00–13:00 | Theres Schrotter Teil 1 | Basic Trainer |
| 17.07.26 | 13:30–15:30 | Carmen M Teil 1 | Intermediate Trainer |
| 18.07.26 | 11:00–13:00 | Theres Schrotter Teil 2 | Basic Trainer |
| 11.09.26 | 13:30–15:30 | Melanie Platz Teil 1 | Basic Trainer |
| 25.09.26 | 13:30–15:30 | Melanie Platz Teil 2 | Basic Trainer |
| 02.10.26 | 13:30–15:30 | Carmen M Teil 2 | Intermediate Trainer |

**Aktuelle Warteliste (unvollständig — mehr kommen noch):**
- Nicole Walemtich
- Svenja Ahrens
- Dori
- Anna-Claudia

---

## Geplantes System

**Empfehlung: WordPress Plugin "Amelia"** (~79€/Jahr)

Ablauf Schülerin:
1. Kalender auf Website öffnen
2. Freien Slot wählen
3. Name + Ausbildungsart + **Google Drive Ordner-Link** eingeben
4. Buchung bestätigt

Ablauf Katarina:
1. Termin + Google Drive Link direkt im Kalender sichtbar
2. Ein Klick → Prüfungsunterlagen öffnen
3. Kontrollieren, Feedback schicken, Zertifikat ausstellen

---

## Was erledigt wurde

- Google Sheets Tabelle ausgelesen und alle Daten rekonstruiert
- Probleme der aktuellen Tabelle identifiziert
- System-Konzept (Amelia + Google Drive Link Integration) besprochen und bestätigt

---

## Offene Punkte / Nächste Schritte

- [ ] **Katarina schickt vollständige Warteliste** — Namen, Ausbildungsart (Basic/Intermediate), Teil (1/2), ggf. verschobene Termine
- [ ] **Katarina gibt verfügbare Prüfungstage/-zeiten an** — für die Planung freier Slots
- [ ] **Saubere Excel-Tabelle bauen** — alle Daten bereinigt, Warteliste integriert, Statusfelder klar
- [ ] **Amelia Plugin einrichten** — Kalender auf WordPress Website einbetten
- [ ] **Custom Field "Google Drive Link"** im Buchungsformular einrichten
- [ ] **Freie Slots für Rest 2026** einpflegen

---

## Technische Notizen

- Google Sheets hat 4 verschiedene Tabellenblöcke — müssen zu einer einzigen sauberen Tabelle zusammengeführt werden
- Warteliste ist als losgeschriebene Namen ohne Struktur — braucht eigenes Tabellenblatt oder Spalte "Status: Wartend"
- Datumsfehler in Original: `11..09.26`, `25..09.26`, `02..10.26` → korrigiert zu `11.09.26`, `25.09.26`, `02.10.26`
