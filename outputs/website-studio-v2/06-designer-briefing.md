# Designer-Briefing — Vertical Kay Studio Website

**Auftraggeberin:** Katarina Tolkmit
**Domain:** verticalkaystudio.com
**Stand:** Mai 2026

---

## Kontext

Dies ist die neue Studio-Website für **Vertical Kay Studio** — Pole Dance, Aerial Hoop & Feminine Movement Studio in Bergheim bei Salzburg.

**Zielgruppe:** Frauen aller Altersgruppen, die wieder in ihren Körper finden möchten. Hauptsächlich aus Salzburg & Salzburg-Umgebung.

**Ziele der Website:**
1. **Markenaufbau** — Vertical Kay als ruhiger, würdevoller, sinnlicher Raum positionieren
2. **Conversion** — Schnupperkurs-Buchungen, Membership-Abschlüsse
3. **SEO/lokale Sichtbarkeit** — Google-Ranking für "Poledance Salzburg"
4. **KI-Findbarkeit** — von ChatGPT, Perplexity, Google AI Overview zitiert werden

**Cross-Linking:** Die Studio-Website wird mit der separaten Ausbildungs-Website **verticalkayeducation.com** verknüpft (Header-Link, Footer, eigene Sektion auf Startseite).

---

## Kontaktdaten Studio (NAP für lokales SEO — überall identisch)

> **Vertical Kay Studio**
> Handelszentrum 16
> 5101 Bergheim bei Salzburg
> Österreich
> Telefon: +43 676 396 0803
> E-Mail: office@verticalkay.de

---

## Brand-Identität

### Farben (verbindlich!)

| Farbe | Hex | Verwendung |
|---|---|---|
| **Magenta** | `#b40087` | Primary, CTAs, Akzente, Hover, Highlights |
| **Light Magenta** | `#cd8bbb` | Sanfte Flächen, Hintergründe, Hover-States |
| **Nude** | `#e1d0d9` | Große Hintergrundflächen, Karten, weiche Sektionen |
| **Schwarz** | `#000000` | Schriftfarbe, Hero-Hintergrund für Fotos |
| **Weiß** | `#ffffff` | Textflächen, Karten, Kontrast |

> **Wichtige Foto-Regel:** Fotos werden mit 40–50% Opacity IMMER auf SCHWARZEM Hintergrund (`#000000`) gelegt — niemals auf hell oder Nude. Sonst verfälschen sich die Farben.

### Typografie (verbindlich aus Canva Brand-Kit)

| Verwendung | Schrift | Details |
|---|---|---|
| **Kopfzeile / Header / Navigation** | **Montserrat** | Sans-Serif, Medium |
| **Titel / Headlines / Hero** | **Cormorant Garamond** | Serif, elegant, sinnlich |
| **Überschriften / Section-Headlines** | **Cormorant Garamond** | Serif |
| **Zwischenschriften / H3** | **Cormorant Garamond** | Serif |
| **Zitate / Testimonials** | **Cormorant Garamond** | Serif Italic |
| **Body-Text** | **Montserrat** | Sans-Serif, klar lesbar |
| **Sublines / kleinere Untertitel** | **Montserrat** | Sans-Serif |
| **Buttons** | **Montserrat** | Sans-Serif, Medium oder SemiBold |
| **Footer-Text** | **Montserrat** | Sans-Serif |
| **Akzent-Sublines (kursiv)** | **Cormorant Garamond Italic** | Für emotionale Brand-Momente |

**Beide Schriften sind auf Google Fonts kostenlos verfügbar:**
- [Cormorant Garamond](https://fonts.google.com/specimen/Cormorant+Garamond) (alle Schnitte)
- [Montserrat](https://fonts.google.com/specimen/Montserrat) (alle Schnitte)

**Empfohlene Schnitte (zum Einbetten):**
- Cormorant Garamond: Light (300), Regular (400), Medium (500), SemiBold (600) + Italic-Varianten
- Montserrat: Regular (400), Medium (500), SemiBold (600), Bold (700)

**Größenhierarchie:** großzügig, viel Luft. Bei Body-Text mind. 16px (Mobile 17px für Lesbarkeit).

### Tonalität & Wirkung

- **sinnlich, weich, elegant, luxuriös**
- **NICHT:** laut, plakativ, fitness-mäßig, "Marketing-Sprech"
- Eher Parfüm-Werbespot als Fitnessstudio-Flyer
- Markenmoment: *"Ich kenne meine Kraft. Ich muss sie nicht beweisen."*

### Visuelle Prinzipien

- **Viel Weißraum** — keine zusammengequetschten Blöcke
- **Großzügige Abstände**
- **Keine Tabellen, keine Textwüsten**
- Übergangs-Sektionen **zentriert**, max. 600–700px breit
- Karten/Sektionen "atmen lassen"
- Buttons: weich abgerundet (8–12px Radius)

### Bildsprache

- **Mood:** ruhig, sinnlich, geerdet, weich aber präsent
- **Vermeiden:** Action-Shots, krasse Tricks, "Instagram-Sexy", harte Fitness-Ästhetik
- **Stattdessen:** Stehen an der Pole, Floorwork, langsamer Spin, ruhige Blicke
- **Licht:** weich, warm (Golden Hour)
- **Outfit:** schlicht, hochwertig, körpernah aber nicht übertrieben sexy
- **Blick:** weich, oft nicht direkt in die Kamera

---

## Technische Anforderungen

### Plattform

- **WordPress** (Katarina nutzt das bereits)
- Theme-Empfehlung: **Astra**, **Kadence** oder **Blocksy** (alle leicht anpassbar) + Elementor oder Bricks Builder
- ALTERNATIV: Webflow, Wix Studio (falls Designer das bevorzugt — bitte mit Katarina klären)

### Pflicht-Features

- [ ] Responsive Design (Mobile-first!)
- [ ] Schnelle Ladezeiten (Core Web Vitals: LCP < 2.5s)
- [ ] HTTPS / SSL-Zertifikat
- [ ] Cookie-Consent-Lösung (DSGVO-konform — Two-Click für iFrames)
- [ ] Google Analytics 4 + Search Console Anbindung
- [ ] Newsletter-Anbindung (z.B. Mailchimp, Brevo)
- [ ] Kontaktformular mit DSGVO-Checkbox
- [ ] WhatsApp-Direktbutton (mobile, klickbar zum Chat)
- [ ] Sticky CTA-Button "Schnupperkurs buchen" am unteren Bildrand (Mobile)

### Buchungssystem-Integration

→ siehe `05-eversports-integration.md` für Details

**Kurz:** Eversports-iFrames auf 5 Seiten einbetten:
1. Stundenplan (volle Wochenansicht)
2. Schnupperkurs (gefiltert)
3. Mitgliedschaft & Preise (Membership-Buchung)
4. Workshops (gefiltert)
5. Optional: Kurs-Unterseiten (Mini-iFrames)

**Buttons mit Eversports-Direktlinks** auf der ganzen Seite verteilt.

### SEO-technische Anforderungen

- [ ] sitemap.xml automatisch generiert (z.B. via Yoast, RankMath)
- [ ] robots.txt konfiguriert
- [ ] Canonical-Tags pro Seite
- [ ] OpenGraph + Twitter Card Meta-Tags
- [ ] **JSON-LD Schema** auf jeder Seite:
  - LocalBusiness / SportsActivityLocation (siehe `03-seo-meta-tabelle.md`)
  - Organization (Startseite)
  - FAQPage (Startseite, FAQ-Seite, Unterseiten mit Mini-FAQs)
- [ ] Meta-Title + Meta-Description pro Seite (siehe `03-seo-meta-tabelle.md`)
- [ ] H1/H2/H3-Struktur korrekt (siehe `02-seitenstruktur.md`)
- [ ] Bilder mit beschreibenden `alt`-Tags
- [ ] Interne Verlinkung zwischen verwandten Seiten

---

## Übergabe-Pakete (was du als Designer bekommst)

### Vom Workspace `outputs/website-studio-v2/`:

| Datei | Inhalt |
|---|---|
| `01-sitemap.md` | Komplette Menüstruktur, alle Seiten, Footer-Aufbau |
| `02-seitenstruktur.md` | Alle Sections pro Seite **mit fertigen Texten** |
| `03-seo-meta-tabelle.md` | Title, Description, Keywords pro Seite + Schema-Codes |
| `04-faqs-startseite.md` | 18 FAQs **mit JSON-LD-Code** für Designer zum Einbauen |
| `05-eversports-integration.md` | Wo iFrames hin, wie sie konfiguriert werden |
| `06-designer-briefing.md` | **Dieses Dokument** — Hauptbriefing |

### Was Katarina noch liefert (bitte einfordern!)

- [ ] **Logo** in mehreren Formaten (SVG, PNG, transparent, schwarz, magenta)
- [ ] **Bildmaterial:** Studio-Fotos, Katarina-Portraits, Kurs-Aufnahmen (alle in hoher Auflösung)
- [ ] **Eversports Studio-ID** + Zugang oder Embed-Codes
- [ ] **Telefonnummer + E-Mail** (für Kontaktseite + Schema)
- [ ] **Geo-Koordinaten** des Studios (Google Maps → Rechtsklick → Koordinaten)
- [ ] **Canva-Brand-Kit Zugriff** für Designer (optional — enthält Logos, Farben, Schriften)
- [ ] **Echte Testimonials** (3 Stück, mit Erlaubnis der Schülerinnen)
- [ ] **Social Media Links** (Instagram, TikTok, YouTube)
- [ ] **Impressum, Datenschutz, AGB** (rechtlich von Katarina/Anwalt)

---

## Reihenfolge der Umsetzung (Empfehlung)

### Phase 1 — Setup (Woche 1–2)
1. Domain `verticalkaystudio.com` bei Hoster anlegen
2. WordPress installieren + SSL-Zertifikat
3. Theme + Page Builder einrichten
4. Brand-Farben und Typografie als Theme-Defaults setzen

### Phase 2 — Kernseiten (Woche 3–5)
1. **Startseite** (priorisieren — hier passiert die meiste Conversion)
2. **Schnupperkurs**
3. **Mitgliedschaft & Preise**
4. **Stundenplan** (mit Eversports-iFrame)
5. **Über uns**
6. **Kontakt**

### Phase 3 — Unterseiten (Woche 6–7)
1. **Poledance Anfänger Salzburg** (SEO-Hauptseite!)
2. Alle weiteren Kurs-Unterseiten
3. Workshops
4. JGA, Privatunterricht

### Phase 4 — SEO & Feinschliff (Woche 8)
1. JSON-LD Schemas einbauen
2. Meta-Titles + Descriptions pflegen
3. Bilder optimieren (alt-Tags, WebP-Format)
4. Google Analytics + Search Console anbinden
5. Google Business Profile anlegen
6. Test auf allen Geräten + Pagespeed-Audit

### Phase 5 — Launch (Woche 9)
1. Final-Check (alle Links, alle Buchungs-Buttons, Cookies, DSGVO)
2. 301-Redirects von alter Studio-Website (falls vorhanden)
3. Sitemap.xml an Google Search Console submitten
4. Launch-Ankündigung Social Media

---

## Wichtige Warnungen für Designer

### ❌ NICHT machen

1. **Keine Beige/Gold-Farbpalette** — auch wenn frühere Briefings das vorschlugen. Brand-Farbe ist **Magenta `#b40087`**.
2. **Keine Stockfotos** mit "Sexy-Pole-Look" — passt nicht zur Marke.
3. **Keine grellen Farben oder Neon-Pinks** — Magenta ist tief und elegant, nicht knallig.
4. **Keine Fitness-Ästhetik** (keine Hanteln, keine "Power"-Sprache).
5. **Kein lautes Marketing** ("Jetzt kaufen!", "Limited Offer!") — passt nicht.
6. **Keine zusammengequetschten Layouts** — die Marke braucht Atem.

### ✅ Ja machen

1. **Viel Weißraum**, großzügige Abstände
2. **Sanfte Übergänge** zwischen Sektionen
3. **Hochwertige Foto-Behandlung** (Schwarzfilter, 40–50% Opacity wo nötig)
4. **Mobile-first** — sehr viele Kund:innen kommen vom Handy
5. **Schnupperkurs-Button mindestens 3–4× pro Seite** sichtbar
6. **JSON-LD Schemas zwingend einbauen** (für SEO + KI-Findbarkeit)

---

## Erfolgs-Messung (KPIs)

Nach 3 Monaten Live-Gang messen:

- [ ] **Schnupperkurs-Buchungen pro Monat** (Hauptmetrik)
- [ ] **Membership-Conversions** (Schnupperkurs → 10er → Membership)
- [ ] **Google-Ranking** für "Poledance Salzburg" (Ziel: Top 3)
- [ ] **Organische Besucher pro Monat** (via Google Analytics)
- [ ] **Sichtbarkeit auf Google Maps** (lokale Suchen)
- [ ] **Erwähnungen in KI-Engines** (manuell prüfen: Frag ChatGPT/Perplexity "Wo kann ich in Salzburg Poledance lernen?")

---

## Zeitplan & Budget

**Bitte besprechen mit Designer:**

- Wie viele Wochen brauchst du?
- Wie viele Iterationsschleifen sind im Angebot enthalten?
- Stundensatz oder Pauschale?
- Wer pflegt die Seite nach Launch (Updates, neue Workshops, Content)?

---

## Bei Fragen

Direkter Ansprechpartner: **Katarina Tolkmit** — `katarina@tolkmit.de`

Oder über Vertical Kay direkt:
- Instagram: [@verticalkay] (Platzhalter)
- WhatsApp: [Nummer]
- Studio-E-Mail: [Platzhalter]

---

## Anhang — Kompakte Sitemap-Übersicht

```
verticalkaystudio.com
├── /                                  Startseite
├── /kurse                             Kurse Übersicht
│   ├── /poledance-anfaenger-salzburg ⭐ SEO-Hauptseite
│   ├── /poledance-foundations
│   ├── /poledance-intermediate
│   ├── /poledance-advanced
│   ├── /masterclass
│   ├── /aerial-hoop-salzburg          ⭐ Zweite SEO-Säule
│   ├── /sensual-heels-pole-flow
│   ├── /chair-dance
│   └── /stretching-bodywork
├── /workshops                         Workshops Übersicht
├── /schnupperkurs                     Erstkontakt-Buchung
├── /stundenplan                       Eversports-iFrame
├── /mitgliedschaft-preise             Preise + Buchung
├── /privatunterricht                  Anfrage 1:1
├── /jga                               JGA-Anfrage
├── /ueber-uns                         Markenstory + Methode
├── /kontakt                           Anfrage + Anfahrt
├── /faq                               Vollständige FAQs
├── /impressum
├── /datenschutz
└── /agb
```
