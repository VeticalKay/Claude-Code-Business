# Session-Zusammenfassung — 30. April 2026

## Was wurde erledigt

### Tally Feedback-Formular — "Feedback Trainingsplan 01"

Katarina testet Trainingsplan 01 bei ihren Schülerinnen und wollte ein digitales Feedback-Formular, das per WhatsApp-Link geteilt werden kann.

**Tally API — Technische Lösung gefunden:**

Nach längerer Debugging-Session wurde die korrekte Block-Struktur für Multiple-Choice-Fragen in der Tally API ermittelt:

- `isFirst` und `isLast` müssen im **Payload** der MC-Option stehen (nicht auf Block-Ebene)
- Erste Option: `payload.isFirst=true, isLast=false`
- Letzte Option: `payload.isFirst=false, isLast=true`
- Block-Level `isFirst=false` für alle MC-Optionen

**Formular erstellt:**

| Feld | Wert |
|------|------|
| Name | Feedback Trainingsplan 01 – VerticalKay |
| Tally Form ID | Bz8KGK |
| Öffentlicher Link | https://tally.so/r/Bz8KGK |
| Status | PUBLISHED |

**12 Fragen:**
1. Gesamtbewertung (1–5, Multiple Choice)
2. Trainingsdauer (MC)
3. Zeitbudget passend? (MC)
4. Häufigkeit pro Woche (MC)
5. Länge der Einheiten (MC)
6. Kurzversion gewünscht? (MC)
7. Übungen klar verständlich? (MC)
8. Flow & Aufbau (MC)
9. Anzahl der Übungen (MC)
10. Was hat dir gut gefallen? (Freitext)
11. Was würdest du dir anders wünschen? (Freitext)
12. Weiterempfehlung? (MC)

### Entscheidung: Wechsel zu Google Forms

Tally verlangt Bezahlung für Design-Anpassungen (Farben, Logo). Katarina entscheidet sich für **Google Forms** statt Tally — kostenlos, mobil-freundlich, automatische Antwort-Sammlung per Google Tabelle.

Alle 12 Fragen wurden als fertige Liste aufbereitet zum manuellen Eintragen in Google Forms.

---

## Offene Punkte / Nächste Schritte

### Kurzfristig
- **Google Forms Formular anlegen**: Katarina trägt die 12 Fragen manuell ein (ca. 10 Min.) → Link per WhatsApp an Schülerinnen
- **Tally-Formular löschen** (optional, da nicht genutzt): Im Tally-Account unter forms.tally.so

### Mittelfristig
- **Logo-Integration**: VK-Monogramm in alle 8 Canva-Trainingspläne einfügen (neues PNG liegt im Canva Brand Kit)
- **Plans 09–12**: Weitere Trainingspläne noch nicht erstellt
- **Website**: Prüfungskalender + WhatsApp-Button dringend

### Langfristig
- Buchprojekte (Affären-Buch, Feminity vs. Feminism)
- /shutdown + GitHub Setup vollständig einrichten

---

_Nächste Session: `/prime` ausführen zum Laden des Kontexts._
