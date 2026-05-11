# Session-Zusammenfassung — 11.05.2026 — Aerial Hoop Basic Trainer Online-Kurs

## Was wurde besprochen

Katarina möchte ihre **Aerial Hoop Basic Trainer Ausbildung** (bisher PDF mit Texten, Bildern und Video-Links) als Online-Kurs auf **Alfima.io** anbieten — in **drei Format-Varianten**:

- **Selbstlerner** (490 €) — reine Plattform
- **Online Hybrid** (590 €) — Plattform + 3 Zoom-Termine
- **Präsenz** (750 €) — Plattform + 1 Zoom + 2 Studio-Termine

Voraussetzung: ca. 1 Jahr Hoop-Eigenpraxis. Prüfung: Theorie schriftlich + Praxis live/online (Korrektur Katarina + Claude).

## Was wurde erledigt

### 1. Quellmaterial analysiert
- **Theorie-PDF** (24 Seiten) komplett gelesen — Rechtliches, Material, Aufhängung, Erste Hilfe, Gesundheit, History, Orientierung, Trainingstheorie, Warm-up, Cool-down, Stundenaufbau
- **Praxis-PDF** (80 Seiten, 31 MB) per Subagent strukturiert in `outputs/aerial-hoop-basic-trainer/_skript-praxis-extrakt.md` (1.648 Zeilen)
- **Drive-Videoordner** "Video's" durchgesehen — 38 Unterordner pro Figur
- **Alfima-Plattform** analysiert: Features für Module/Lektionen, Termine (Zoom), E-Mail Marketing, Online-Kurs-Generator vorhanden

### 2. Master-Implementierungsplan erstellt
`plans/2026-05-11-aerial-hoop-basic-trainer-alfima.md`
- 13 Module mit insgesamt **~95 Lektionen** einzeln aufgelistet
- Mapping pro Lektion: Skript-Quelle ↔ Drive-Videoordner
- 33 Implementierungs-Schritte in 6 Phasen (Beispiel-Lektion → Setup → Videos → Inhalte → Drumherum → Launch)
- 7 offene Entscheidungsfragen für Katarina
- ⚠️ **Lücke aufgedeckt:** ~20 Figuren im TOC haben kein Cueing im aktuellen Praxis-Skript (Modul 9 als Erweiterung markiert)

### 3. Beispiel-Lektion ausgearbeitet als Format-Vorlage
`outputs/aerial-hoop-basic-trainer/lektionen/M4-L02_step-in-mount-standard.md`
- Komplette Lektion zum 1:1-Reinkopieren in Alfima
- Format: Lernziel · Video · Anatomie · Schritt-für-Schritt (Originalwortlaut) · Cueing-Notes · Häufige Fehler · Progression · Mini-Quiz (3 Fragen) · Download-Hinweis · verlinkte Lektionen · Trainer-Notiz

### 4. Level-1/2-Strategie entschieden
- **Empfehlung Claude:** EIN Kurs jetzt, innerhalb Modul sortiert (erst L1, dann L2 → spätere Trennung in 2 Kurse = 4-5 Stunden Aufwand)
- **Katarina:** Geht im Canva-Skript bis Sonntag 17.05. durch und entscheidet — Claude kann via MCP-Anbindung dann automatisch trennen (Markierungen einfügen ODER Skript duplizieren)

### 5. Memory aktualisiert
Zwei neue Memory-Einträge erstellt:
- `user_ausbildung_preise.md` — Preisliste alle Ausbildungen × Formate (aus Canva-Doc)
- `user_ausbildung_formate.md` — Format-Struktur der drei Varianten (Selbstlerner/Hybrid/Präsenz)

## Offene Punkte / Nächste Schritte

### Bis Sonntag 17.05.2026 — Katarina
- **🔥 Aerial Hoop Trainer Level 1/2 Entscheidung im Canva-Skript** — durchgehen, mental oder mit Kommentaren markieren wo die Trennung sein soll
- **Beispiel-Lektion 4.2 (Step in Mount) reviewen** — passt das Format? Tonalität? Quiz-Stil?

### Sobald Level-Entscheidung steht — Claude
- Skripte in Canva trennen (Markierungen einfügen ODER Duplizieren je nach Entscheidung)
- Master-Plan an Level-Struktur anpassen falls nötig

### 7 offene Entscheidungsfragen aus dem Plan
1. Videos → Alfima direkt oder YouTube unlisted Embed?
2. Sind alle Module in allen 3 Format-Varianten enthalten?
3. Modul 9 (Lücken): nachholen / nur Video / skippen?
4. Theorieprüfung-Format: Multiple Choice / Freitext / Mix?
5. Zertifikat-Aussteller (V-Gym Education?) + Design?
6. Rhythmus der 3 Zoom-Calls beim Hybrid (Monat 1/2/3?)
7. Selbstlerner-Q&A als Upsell-Hook?

### Nach Format-Validierung — Phase D im Plan
- Alle ~95 Lektionen seriell im gleichen Format ausarbeiten
- Cueing-Karten als PDF designen (Canva, Brand-Farben)
- Theorieprüfung-Fragenkatalog
- Verkaufs-Landingpages in Alfima (3 Varianten)
- Videos zu Alfima hochladen

## Wichtige Erkenntnisse

- **Alfima ist die richtige Plattform** — Online-Kurs-Generator, Module/Lektionen, Termine (Zoom), E-Mail Marketing, alles vorhanden. Katarina hat PRO-Account.
- **Drei Format-Varianten = drei Alfima-Produkte** mit gleicher Modul-Basis, Unterschied nur Live-Zugang
- **Drive-Videoordner sind schon perfekt benannt** — direkt mappbar zu Lektionen
- **Praxis-Skript hat eine Lücke** ab Seite 80 — letzte ~20 Figuren fehlen (Cueing-Text). Bei Modul 9 transparent gemacht.
- **Skript-Wortlaut ist wertvoll** — bei der Extraktion 1:1 übernommen (nicht umformuliert)
