# Eversports-Integration — Vertical Kay Studio

**Ziel:** Buchungssystem nahtlos in die Website einbetten — Kunde bleibt auf verticalkaystudio.com.

---

## Was ist ein iFrame? (Erinnerung)

Ein iFrame ist ein "Fenster" auf deiner Website, das Inhalte einer anderen Seite einbettet. Eversports stellt dafür einen Code-Schnipsel bereit, den dein Designer in die jeweilige Seite einbaut.

**Vorteile gegenüber Verlinkung:**
- Kunde verlässt deine Domain nicht (besser fürs SEO + niedrigere Absprungrate)
- Optisch wirkt es wie deine Seite
- Kurse, Verfügbarkeit und Preise immer aktuell ohne manuelle Pflege

---

## Wo welche iFrames eingebaut werden

| Seite | iFrame-Inhalt | Zweck |
|---|---|---|
| **Stundenplan** (`/stundenplan`) | Eversports Wochenkalender (volle Ansicht) | Hauptbuchungs-Hub |
| **Schnupperkurs** (`/schnupperkurs`) | Eversports Termine "Schnupperkurs" gefiltert | Direkte Buchung Erstkontakt |
| **Mitgliedschaft & Preise** (`/mitgliedschaft-preise`) | Eversports Membership-Buchung pro Karte | "Platz sichern"-Buttons führen zu Eversports-Anmeldung |
| **Workshops** (`/workshops`) | Eversports Workshop-Termine gefiltert | Workshop-Buchung |
| **Kurs-Unterseiten** (z.B. `/kurse/poledance-foundations`) | Optional: Mini-iFrame mit nächsten Terminen für diesen Kurs | Direkter CTA |
| **Startseite — Sektion 6 Stundenplan-Teaser** | Mini-Vorschau Eversports (kompakt) ODER Bild + Button | Engagement |

---

## So bekommt dein Designer die iFrame-Codes

### Option 1: Eversports Studio-Backend

1. Login bei [eversports.com](https://www.eversports.com) mit deinen Studio-Zugangsdaten
2. **Einstellungen → Integrationen → Widget / Embed Code**
3. Dort gibt es fertige Code-Snippets für:
   - Wochenplan-Widget
   - Einzelne Kurs-Widgets
   - Membership-Buchungs-Widget
   - Schnupperkurs-Widget

### Option 2: Eversports-Support kontaktieren

E-Mail: `support@eversports.com`
Bitte konkret nach **"Embed-Code für Webseite mit individueller Filterung"** fragen.

### Option 3: Dein Designer macht es

Schick deinem Designer:
- Eversports-Login (oder lass ihn die Codes selbst generieren)
- Die Liste oben (welche Seiten welche iFrames brauchen)
- Brand-Farben, damit er das Widget farblich anpasst (Eversports erlaubt CSS-Customizing)

---

## Generischer iFrame-Code (Beispiel)

So sieht ein typischer Eversports-Embed-Code aus:

```html
<iframe
  src="https://www.eversports.com/widget/calendar?facility_id=DEIN_STUDIO_ID&primary_color=b40087"
  width="100%"
  height="800"
  frameborder="0"
  style="border: none;">
</iframe>
```

**Wichtige Parameter:**
- `facility_id` — deine Studio-ID bei Eversports (bekommst du im Backend)
- `primary_color` — Magenta `b40087` (ohne #) für Brand-Konsistenz
- `width` — immer 100% für responsive Layouts
- `height` — anpassen je nach Sektion

---

## Design-Konsistenz

### Eversports-Widget farblich anpassen

Eversports erlaubt CSS-Customization für eingebettete Widgets. Designer soll:
- Primary Color = `#b40087` (Magenta)
- Buttons = Magenta-Stil wie Rest der Website
- Schriftart = wenn möglich auf Body-Font der Website abstimmen

### Falls Eversports zu wenig Customizing zulässt

**Plan B:** Eversports-Widget in einem **Container mit Brand-Hintergrund** (Nude `#e1d0d9` oder weiß) einbetten — so wirkt der Übergang weicher.

---

## Buchungs-Buttons — wohin verlinken

Auf den Buttons der Website werden Eversports-Direktlinks hinterlegt:

| Button | Verlinkung |
|---|---|
| `Schnupperkurs buchen` | Eversports Schnupperkurs-Buchungsseite (Direktlink) |
| `Platz sichern` (Memberships) | Eversports Membership-Anmeldung (jeweilige Membership) |
| `Jetzt starten` (10er Block) | Eversports 10er-Block Kauf |
| `Workshop buchen` | Eversports Workshop-Termin |
| `Privatstunde anfragen` | Kontaktformular (KEIN Eversports — das läuft individuell) |
| `JGA anfragen` | Kontaktformular |

**Wichtig:** Frag deinen Designer, ob er die Buttons mit `target="_blank"` öffnet (neuer Tab) oder im selben Tab.
- **Empfehlung:** Im selben Tab, wenn iFrame eingebettet ist (Kunde bleibt im Flow).
- Bei externen Direktlinks zu Eversports: Neuer Tab, damit deine Seite im Browser bleibt.

---

## Datenschutz (DSGVO) — wichtig!

Eversports-iFrames laden Inhalte von einer Drittseite — das ist DSGVO-relevant.

**Dein Designer muss:**
1. **Cookie-Consent** einbauen (z.B. Borlabs Cookie, Cookiebot, Iubenda)
2. iFrames erst nach **aktiver Zustimmung** laden (sog. "Two-Click-Solution")
3. **Datenschutzerklärung** ergänzen mit Hinweis auf Eversports-Einbettung
4. Eversports als Auftragsverarbeiter im Datenschutz-Verzeichnis nennen

**Beispiel-Text für Datenschutzerklärung:**
> Auf unserer Website binden wir das Buchungssystem von Eversports (Eversports GmbH, Deutschland) ein. Bei Aufruf einer Seite mit eingebettetem Eversports-Widget werden Daten an Eversports übertragen. Mehr Infos: [Eversports Datenschutz](https://www.eversports.com/datenschutz)

---

## Fallback: Wenn iFrame nicht klappt

Falls aus technischen Gründen der iFrame nicht eingebettet werden kann (z.B. Eversports-Beschränkung, DSGVO-Konflikt), nutze **Direkte Verlinkung** als Fallback:

> `Termin buchen →` (Button öffnet `https://www.eversports.com/dein-studio` in neuem Tab)

**Nachteil:** Kunde verlässt deine Seite. Höhere Absprungrate.

---

## Checkliste für Designer

- [ ] Studio-ID bei Eversports klären (von Katarina einholen)
- [ ] Embed-Codes für alle 5 Seiten generieren
- [ ] Widgets farblich anpassen (Magenta `#b40087`)
- [ ] Cookie-Consent-Lösung wählen + Two-Click-Logik einbauen
- [ ] Datenschutzerklärung erweitern (Eversports erwähnen)
- [ ] Mobile-Optimierung der iFrames testen (volle Breite, lesbare Schrift)
- [ ] Pagespeed prüfen (iFrames können langsam laden — eventuell Lazy-Loading)
- [ ] Alle Buchungs-Buttons mit korrekten Eversports-Links verknüpfen
- [ ] Test-Buchungen durchführen (Schnupperkurs, Membership, Workshop)

---

## Alternativen zu Eversports (falls relevant)

Falls in der Zukunft ein Wechsel überlegt wird, hier die Optionen mit gutem WordPress-Support:

- **Bookly** (WordPress-Plugin, sehr flexibel)
- **Amelia** (WordPress-Plugin, gutes Design)
- **Calendly** (für Privatstunden, nicht für Gruppen)
- **Mindbody** (Profi-Lösung, teurer)

**Empfehlung:** Bei Eversports bleiben — du nutzt es schon, deine Kund:innen sind daran gewöhnt, und es funktioniert.
