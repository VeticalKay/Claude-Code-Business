# Feedback Workflow — Theorie-Prüfungen

## Aufgabenteilung
- **Claude (Agent)** → Theorie-Feedback erstellen
- **Katarina** → Praxis-Feedback (NIEMALS anfassen, nicht lesen, nicht bearbeiten!)
- Katarina kombiniert Theorie + Praxis am Ende selbst

## Ordnerstruktur Google Drive
Jede Schülerin hat einen **eigenen persönlichen Ordner** in Google Drive.
Die Theorie-Datei kommt direkt in diesen Ordner — NICHT in "Feedbacks bearbeitet".

Bekannte Schülerinnen-Ordner:
- Lea Sophie Pohle: `1cPQqFuO5NxadIY6Av6uOSMEYVbG63rHf`

Prüfungs-PDFs der Schülerinnen liegen in deren eigenen Ordnern (geteilt mit Katarina).

## Datei erstellen — korrekter Workflow
1. PDF der Schülerin lesen (`read_file_content` oder `download_file_content`)
2. Feedback als HTML aufbereiten (V5-Template, siehe unten)
3. `create_file` mit `contentMimeType: "text/html"` → wird zu echtem Google Doc
4. **Prüfen**: Zurückgegebenes `mimeType` muss `application/vnd.google-apps.document` sein
   - ❌ `text/html` → Fehler melden, NICHT weitermachen
5. `copy_file` in den **Schülerinnen-Ordner** (`parentId` = Ordner der Schülerin)
6. Katarina löscht das Original aus Mein Drive manuell (kein Delete-Tool im MCP)

## Feedback-Template V5 (HTML-Struktur)
```html
<h1><strong>Feedback Theorie Teil X — [Vorname Nachname]</strong></h1>
<p><strong>Gesamtpunktzahl: XX / XXP</strong></p>
<p>&nbsp;</p>
<p>Hallo liebe [Vorname],</p>
<p>[Persönlicher Einleitungstext — empathisch, wertschätzend, Mentor-Sprache]</p>
<p>&nbsp;</p>
<hr>
<p>&nbsp;</p>

<!-- Pro Aufgabe: -->
<p><strong><u>Aufgabe X (X / XP) — [Aufgabentitel]</u></strong></p>
<p>&nbsp;</p>
<p><em><u>Positive Aspekte:</u></em></p>
<ul><li>...</li></ul>
<p>&nbsp;</p>
<p><em><u>Bitte noch beachten, betonen und verinnerlichen:</u></em></p>
<ul><li>...</li></ul>

<p>&nbsp;</p><hr><p>&nbsp;</p>
<!-- nächste Aufgabe ... -->

<p><strong>Gesamtpunktzahl: XX / XXP</strong></p>
```

## Abschnitts-Labels (EXAKT so — keine Abkürzungen!)
- ✅ `Positive Aspekte:`
- ✅ `Bitte noch beachten, betonen und verinnerlichen:` ← NICHT kürzen!

## Ton & Sprache
- Empathisch, freundlich, auf Augenhöhe
- Mentor-Sprache, nicht Beurteilungssprache
- "schön wäre noch...", "du könntest...", "hier steckt noch Potenzial"
- KEIN klinischer, distanzierter Ton

## Punktestruktur Basic Trainer Theorie
- Teil 1 (33P): A1–A8 = 2P, A9 = 4P, A10–A12 = 3P, A13–A14 = 2P
- Teil 2 (20P): je nach Aufgabenblatt

## Wichtig für den Agenten
- Praxis-Dokumente der Schülerin NIEMALS öffnen, lesen oder bearbeiten
- Nur Theorie-PDFs verarbeiten
- Neue PDFs erkennen: Dateiname enthält "Theorie" oder "Teil 1" / "Teil 2"
- Nach dem Erstellen: Datei-ID und Ordner in Session-Output dokumentieren
