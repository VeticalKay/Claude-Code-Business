# Session-Zusammenfassung — 27. April 2026

## Was wurde besprochen

### Prüfungskalender für die Website
Katarina möchte einen Buchungskalender für Prüfungstermine auf ihrer WordPress-Website einbinden, mit folgenden Anforderungen:
- Freie Prüfungstermine sichtbar und buchbar
- Max. 1 Teilnehmer pro Termin
- Teilnehmer trägt Prüfungsart selbst ein (verschiedene Arten, aber keine getrennten Termine)
- Nur für Ausbildungsteilnehmerinnen
- Buchung kostenlos, manuelle Bestätigung durch Katarina
- Google Drive Link für Prüfungsunterlagen kann nachträglich eingereicht werden
- Prüfungsdauer: ca. 2 Stunden

### Tool-Vergleich: Amelia Lite vs. Calendly
Detaillierter Vergleich beider Optionen für Katarinas spezifische Anforderungen.

### Netlify-Klärung
Katarina fragte nach Netlify als Alternative — wurde geklärt dass Netlify eine Hosting-Plattform ist, kein Buchungstool. Wahrscheinliche Verwechslung mit Calendly.

---

## Was wurde erledigt

- Anforderungen für den Prüfungskalender vollständig aufgenommen
- Vollständiger Step-by-Step Setup-Plan für **Amelia Lite** (WordPress Plugin) erstellt:
  - Plugin installieren
  - Service anlegen (Prüfungstermin, 120 Min, Kapazität 1, kostenlos)
  - Manuelle Bestätigung aktivieren (Default status: Pending)
  - Custom Fields einrichten (Prüfungsart = Pflicht, Google Drive Link = optional)
  - Termine manuell anlegen
  - Einbindung per Gutenberg Block oder Shortcode `[ameliabooking service=1]`
- Lösung für Google Drive Link nachträglich: per E-Mail an katarina@tolkmit.de mit Betreff-Schema
- Vergleichstabelle Amelia Lite vs. Calendly erstellt

---

## Empfehlung / Ergebnis

**Amelia Lite** ist die beste Option:
- Kostenlos
- Manuelle Bestätigung möglich (bei Calendly nur kostenpflichtig)
- Custom Fields möglich (bei Calendly nur kostenpflichtig)
- Daten bleiben auf eigenem Server (DSGVO-konform)
- Direkte WordPress-Integration

---

## Offene Punkte / Nächste Schritte

- [ ] Amelia Lite Plugin installieren & einrichten (Katarina macht es selbst)
- [ ] Erklärungstext für die Prüfungstermin-Seite formulieren (Claude kann liefern)
- [ ] Bestätigungs-E-Mail Text formulieren (mit Hinweis auf Google Drive Link Einreichung)
- [ ] Unterseite `/prüfungstermine` auf WordPress anlegen und Kalender einbinden
- [ ] Erste Prüfungstermine in Amelia eintragen
