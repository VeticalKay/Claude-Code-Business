# Website-Text: Kontakt

**Seite:** verticalkaystudio.com/kontakt
**Stil:** Cormorant Garamond Headlines, Montserrat Body — einladend, persönlich, warm

---

## SEKTION 1 — HERO

**Headline (Cormorant Garamond, mittlere Größe):**
> Sag Hallo. Wir freuen uns.

**Subline (Montserrat, kursiv):**
> *Egal ob du Fragen hast, einen Termin vereinbaren oder einfach Hallo sagen möchtest — wir antworten dir gerne.*

---

## SEKTION 2 — KONTAKTDATEN

**Headline:**
> So erreichst du uns.

**2-Spalten-Layout (oder untereinander auf Mobile):**

### Spalte 1 — Adresse & Anfahrt

**🌸 Vertical Kay Studio**

Handelszentrum 16
5101 Bergheim bei Salzburg
Österreich

→ **Mit dem Auto:** Parkplätze direkt am Studio
→ **Mit Öffis:** ab Salzburg Hauptbahnhof ca. 15 Min

### Spalte 2 — Direkt schreiben

**🌸 Telefon & WhatsApp**
[+43 676 396 0803](tel:+436763960803)

**🌸 E-Mail**
[office@verticalkay.de](mailto:office@verticalkay.de)

**Buttons (zwei nebeneinander):**
- Primary: `WhatsApp schreiben` (Link: https://wa.me/436763960803)
- Secondary: `E-Mail schreiben` (mailto:office@verticalkay.de)

---

## SEKTION 3 — GOOGLE MAPS EMBED

**Hinweis für Designer:**
- Google Maps iFrame mit Adresse `Handelszentrum 16, 5101 Bergheim bei Salzburg`
- Geo-Koordinaten: `47.841315, 13.039991`
- Höhe: ca. 350px
- Mit Cookie-Consent vor Laden (DSGVO)
- Brand-Akzent: feiner Magenta-Rand um den iFrame

---

## SEKTION 4 — ÖFFNUNGSZEITEN

**Headline:**
> Wann ist das Studio geöffnet?

**Body:**
> Unser Studio öffnet **nach Kursplan**. Den aktuellen Stundenplan findest du auf unserer [Stundenplan-Seite](/stundenplan).
>
> Für Privatunterricht, JGA oder Beratungstermine vereinbaren wir individuelle Zeiten — schreib uns einfach.

---

## SEKTION 5 — KONTAKTFORMULAR

**Headline:**
> Schreib uns.

**Subline (kurz):**
> *Wir antworten dir innerhalb von 24 Stunden.*

**Formular-Felder:**

- **Name** (Pflicht)
- **E-Mail** (Pflicht)
- **Telefon** (optional)
- **Worum geht es?** (Dropdown):
  - Schnupperkurs buchen
  - Frage zu Mitgliedschaft
  - Privatunterricht-Anfrage
  - JGA-Anfrage
  - Trainer-Ausbildung
  - Etwas anderes
- **Nachricht** (Pflicht, mehrzeilig)
- **Datenschutz-Checkbox** (Pflicht, DSGVO)

**Button:**
> `Nachricht senden`

**Bestätigungstext nach Absenden:**
> *Danke für deine Nachricht. Wir melden uns innerhalb von 24 Stunden bei dir zurück.*

---

## SEKTION 6 — SOCIAL MEDIA

**Headline:**
> Folge uns auf Social Media.

**Body:**
> Auf unseren Kanälen teilen wir Einblicke ins Studio, Workshop-Termine, neue Kurse und kleine Inspirationen.

**Social-Media-Buttons (Icons + Text):**

🌸 **Instagram** → [@verticalkay] *(Link bitte ergänzen)*
🌸 **TikTok** → [@verticalkay] *(Link bitte ergänzen)*
🌸 **YouTube** → [Vertical Kay] *(Link bitte ergänzen)*

---

## SEKTION 7 — FINALER CTA

**Headline:**
> Bereit, vorbeizukommen?

**Body:**
> Beginne mit einem Schnupperkurs — 60 Minuten, 15 €.

**Button:**
> `Schnupperkurs buchen`

---

# SEO-META

| Element | Wert |
|---|---|
| **H1** | Kontakt — Vertical Kay Studio Salzburg |
| **Title** | Kontakt \| Vertical Kay Studio Salzburg — Bergheim |
| **Meta Description** | Kontakt Vertical Kay Studio: Handelszentrum 16, 5101 Bergheim bei Salzburg. Telefon +43 676 396 0803. Schreib uns auf WhatsApp, per E-Mail oder über das Formular. |
| **Primary Keyword** | Vertical Kay Studio Kontakt |
| **Secondary Keywords** | Pole Studio Salzburg Adresse · Vertical Kay Anfahrt · Pole Studio Bergheim |

---

# LOCALBUSINESS SCHEMA (für Designer, in `<head>` einbinden)

Vollständige Version siehe `03-seo-meta-tabelle.md` — hier kompakt:

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "SportsActivityLocation",
  "name": "Vertical Kay Studio",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Handelszentrum 16",
    "addressLocality": "Bergheim bei Salzburg",
    "postalCode": "5101",
    "addressCountry": "AT"
  },
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": "47.841315",
    "longitude": "13.039991"
  },
  "telephone": "+436763960803",
  "email": "office@verticalkay.de",
  "url": "https://verticalkaystudio.com"
}
</script>
```

---

# DESIGNER-HINWEISE

## Layout
- **Hero kompakt** — keine ganzscreen Höhe nötig
- **Sektion 2 (Kontaktdaten):** 2-Spalten Desktop, untereinander Mobile
- **Google Maps Embed:** mit weichem Rand (kein hartes Rechteck)
- **Kontaktformular:** klar, viele Pflichtfelder vermeiden — nur das Nötigste
- **Bestätigungs-Text** sollte sinnlich-warm sein, nicht funktional

## Wichtig
- **WhatsApp-Button** mit https://wa.me/436763960803 öffnet WhatsApp-Chat direkt
- **mailto:** öffnet E-Mail-Programm
- **tel:** öffnet Telefon-Anruf (auf Mobile)
- **Datenschutz-Checkbox** ist DSGVO-Pflicht — Designer muss verlinkten Datenschutz-Text einbinden

## Mobile-Reihenfolge
1. Hero
2. Kontaktdaten (Adresse + Telefon/E-Mail/WhatsApp)
3. Google Maps (volle Breite)
4. Öffnungszeiten
5. Kontaktformular
6. Social Media
7. Final CTA

## DSGVO
- Google Maps iFrame **erst nach Cookie-Consent** laden
- Vor Consent: Platzhalter mit "Bitte akzeptiere Cookies, um die Karte zu sehen"

---

# VALIDIERUNGS-HINWEISE

- [x] Adresse korrekt: Handelszentrum 16, 5101 Bergheim bei Salzburg
- [x] Telefon korrekt: +43 676 396 0803
- [x] E-Mail korrekt: office@verticalkay.de
- [x] Geo-Koordinaten: 47.841315 / 13.039991
- [ ] **Bitte ergänzen:** Instagram-Link
- [ ] **Bitte ergänzen:** TikTok-Link
- [ ] **Bitte ergänzen:** YouTube-Link
- [ ] **Bitte prüfen:** Öffnungszeiten "nach Kursplan" — möchtest du das so kommunizieren, oder feste Studio-Zeiten?
