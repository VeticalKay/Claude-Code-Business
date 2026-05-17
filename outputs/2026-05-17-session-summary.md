# Session-Zusammenfassung — 17.05.2026

## Was wurde besprochen

Kurze Recherche-Session zum Thema **Eversports-Anbindung an Claude**: Kann ich Eversports mit Claude verbinden, um Classes anzulegen und Kunden per E-Mail anzuschreiben?

## Was wurde erledigt

- **Eversports API-Realität geklärt:** Keine offizielle Claude-/MCP-Integration. Eversports hat eine REST API, die aber **nicht Self-Service** ist — Zugang muss über Support angefragt werden.
- **Eversports Manager Backend geprüft** (Screenshots): Tabs "Berechtigungen & Datenschutz" und "Version & Info" enthalten keinen API-Zugang. Der "O"-Tab ist "Online Übertragung" (Livestream-Setup) — nicht relevant.
- **Klares Vorgehen definiert:**
  1. Eversports Live-Chat / Support kontaktieren → API-Zugang anfragen
  2. Falls API kommt: API-Key + Doku → Claude baut Scripts für Class-Anlage + Kundenexport
  3. Falls nicht: CSV-Export-Route + Brevo (oder Mailerlite) für E-Mail-Marketing
- **Chat-Text für Eversports Support formuliert** (siehe Konversation).
- **Empfehlung für E-Mail-Marketing:** Nicht über Eversports, sondern **Brevo** (EU/DSGVO, gratis bis 300 Mails/Tag) — bessere Templates, Tracking, Abmeldungen, passt zur Brand Voice.

## Offene Punkte / Nächste Schritte

- [ ] **Eversports Support anschreiben** (Live-Chat im Backend) → API-Zugang erfragen
- [ ] Antwort von Eversports zurück an Claude → gemeinsam nächsten Schritt planen
- [ ] **Parallel-Option:** CSV-Export aus Eversports (Kunden) testen → Daten an Claude für Segmentierungs-/Newsletter-Workflow
- [ ] **Brevo-Setup** evaluieren (sobald entschieden ist, ob E-Mails über Eversports gehen oder extern)

## Status

Katarina entscheidet selbst, wie sie weitermacht ("ich werde dann schauen wie ich es mache"). Session beendet.
