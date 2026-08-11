# Karriere-Funnel · Wilfried von Briel Maschinenbau

Mini-Karriereseite für die Stelle **Industrieelektriker (m/w/d) – Elektromontage & Verdrahtung**
(Standort Allensbach). Eine einzige, in sich geschlossene Datei: [`index.html`](index.html) –
kein Build, keine Abhängigkeiten. Aufbau und Funnel-Logik entsprechen der Mauser-Seite
(`saviold/mauser`), Farben und Inhalte sind auf die Briel-CI umgestellt.

**Live (nach Aktivierung von GitHub Pages):** https://saviold.github.io/vonbriel/

## Aufbau der Seite

1. **Topbar** – Wortmarke, Telefonnummer, „Jetzt bewerben"
2. **Hero + Mini-Check** – der Fragebogen ist sofort aktiv (kein Extra-Klick)
3. **Trust-Strip** – Allensbach · Maschinenbau · Vollzeit · Elektromontage
4. **Money-Hook** – Attraktivitäts-Kachel (aktuell „Faire Bezahlung")
5. **Die Stelle im Detail** – Aufgaben · Profil · Wir bieten
6. **Sticky-CTA** (mobil) und **Footer** mit Anschrift & Rechtlichem

## Vorfilter (Knockout-Kriterien)

Der Mini-Check hat 5 Fragen. Drei davon filtern hart vor – wer sie nicht erfüllt, landet auf
einem freundlichen Absage-Screen und wird **nicht** als Lead übertragen (weder E-Mail noch
LeadTable):

| Frage | Voraussetzung | Knockout bei |
|---|---|---|
| 1 · Ausbildung | abgeschlossene Ausbildung als Elektriker (auch im Ausland) | „Nein" / „nur Berufserfahrung" |
| 2 · Schaltplan | Schaltpläne lesen & verstehen (Grundlagen genügen) | „Nein" |
| 3 · Deutsch | mindestens Niveau B1 | „Nur wenige Worte Deutsch (A1/A2)" |

Nicht filternd, nur zur Einschätzung: Frage 4 (Erfahrung in Elektromontage/Schaltschrankbau)
und Frage 5 (Führerschein). Aus den bewerteten Antworten entsteht ein Match-Score
(`Top-Match` / `Guter Match` / `Entwicklungs-Kandidat`), der mit dem Lead übertragen wird.

## Wohin gehen die Bewerbungen?

Beide Wege laufen parallel, siehe `CONFIG` im Script-Teil von `index.html`:

- **LeadTable** – Generic Webhook der Tabelle
  (Kunde `6a6f3bff4c269f23752c643a`, Tabelle `6a6f3c0e960f8695445ed26f`).
  Übertragen werden Name, Telefon, Wunsch-Kontakt, E-Mail, PLZ, frühester Start, Nachricht,
  Match-Score, alle Antworten (lesbarer Key + ASCII-Alias), Kampagnen-Variante und Quelle.
- **E-Mail** – über `formsubmit.co` an `CONFIG.leadEmail`
  (derzeit `savio.roeckle@wave2network.de`, jederzeit auf eine Briel-Adresse umstellbar).
  Nur dieser Weg transportiert einen optional hochgeladenen Lebenslauf als Anhang.

## Mobil & Conversion

Die Seite ist mobil-first gebaut – der Großteil des Ad-Traffics kommt vom Handy:

- **Frage 1 steht im ersten Bildschirm.** Auf 360–430 px Breite sind alle vier
  Antwortmöglichkeiten ohne Scrollen sichtbar (Hero bewusst knapp, Badges als
  Scroll-Reihe, Karte randnah über die volle Breite).
- **Große Tap-Ziele:** Antworten min. 58 px hoch, Kontakt-Umschalter 54 px,
  kein 300-ms-Delay, kein grauer Tap-Blitz, Safe-Area für iPhone-Homebar.
- **Kurzes Formular:** nur Name, Telefon und PLZ sind sichtbar. E-Mail, Start,
  Nachricht und Lebenslauf liegen eingeklappt hinter „Optional hinzufügen".
- **Kein Fortschrittsverlust:** Antworten liegen in der `sessionStorage`. Wer
  die App wechselt oder neu lädt, landet wieder in derselben Frage.
- **Sticky-Button als Wiederaufnahme-Anker:** solange die Karte nicht im Bild
  ist, zeigt er „Weiter – Frage 3 von 5"; nach dem Absenden verschwindet er.
- **Telefon-Ausweg** unter dem Absende-Button – wer nicht tippen will, ruft an.
- **Effekte als Feedback, nicht als Deko:** Haken-Animation auf der gewählten
  Antwort, Richtungs-Animation der Schritte (vor/zurück), Lichtreflex auf dem
  Fortschrittsbalken, kurzes Vibrieren (Android), Einblenden der Inhalte beim
  Scrollen, gezeichneter Erfolgs-Haken. Alles respektiert
  `prefers-reduced-motion`.

### Messbare Funnel-Events

`track()` schickt an Umami/WEBUNDO (`window.umami.track`) und an `window.dataLayer`:
`funnel_view`, `funnel_start`, `funnel_antwort` (mit Frage & Antwort),
`funnel_absage` (mit Grund), `funnel_formular`, `formular_optional_geoeffnet`,
`anruf_klick`, `bewerbung_absenden`, `bewerbung_gesendet`, `bewerbung_fehler`,
`funnel_resume`, `sticky_cta_klick`. Damit lässt sich sehen, an welcher Frage
Bewerber abspringen.

## Fotos (`assets/`)

Die Seite bindet echte Werkstatt- und Team-Bilder ein. **Fehlt eine Datei,
entfernt das Script die Kachel automatisch** (und blendet die Team-Sektion
komplett aus) – die Seite wirkt also nie kaputt. Erwartete Dateinamen:

| Datei | Motiv | Wo es erscheint |
|---|---|---|
| `assets/elektromontage.jpg` | Kollege am offenen Schaltschrank | breites Bild über „Die Stelle im Detail" |
| `assets/team.jpg` | drei Kollegen, Daumen hoch | großes Bild in der Team-Sektion |
| `assets/kollege-zeigt.jpg` | Kollege zeigt in die Kamera | Team-Sektion |
| `assets/kollege-ok.jpg` | Kollege mit OK-Zeichen | Team-Sektion |
| `assets/werkstatt.jpg` | Anlagenmontage in der Halle | Team-Sektion |

Empfehlung: JPG, längste Kante ca. 1600–2000 px, unter 300 KB pro Bild.
Dieselben Dateien nutzen auch die Ad-Creatives.

Die Schriften (Poppins, Inter) liegen ebenfalls unter `assets/fonts/` und werden
selbst gehostet – kein Google-Fonts-Request, also ein Roundtrip weniger auf dem
Handy und kein Datenschutz-Thema.

## Ad-Creatives

Passende Anzeigenmotive in 4:5 und Story/Reels liegen unter
[`creatives/`](creatives/) – fünf Konzepte, gerendert als PNG in
`creatives/png/`. Details, Konzeptliste und Render-Anleitung stehen in
[`creatives/README.md`](creatives/README.md).

## Anpassen

- **Texte/Stelle:** alles im `JOBS`-Objekt (`industrieelektriker`) in `index.html`.
- **Weitere Stelle:** neuen Eintrag nach der Vorlage anlegen und `active: true` setzen –
  bei mehreren aktiven Stellen erscheint automatisch eine Auswahl. Direktlink: `?job=<slug>`.
- **Ad-Varianten (Message-Match):** `heroVariants` – Aufruf über `?v=fit` (Default),
  `?v=region`, `?v=team`.
- **Farben:** CSS-Variablen im `:root`-Block (`--navy`, `--accent`, `--steel`).
- **Logo:** aktuell als Wortmarke in HTML/CSS umgesetzt. Sobald die Original-Datei vorliegt:
  `logo.svg` ins Repo legen und die beiden `<span class="logo__text">…</span>`-Blöcke
  (Topbar und Footer) durch
  `<img class="logo__img" src="logo.svg" alt="Wilfried von Briel Maschinenbau" />` ersetzen.

## Offene Punkte (mit Briel abstimmen)

Im Quelltext jeweils als `TODO` markiert:

- **Benefits-Liste** („Wir bieten") ist allgemein gehalten – echte Leistungen eintragen.
- **Money-Hook**: falls es Urlaubs-/Weihnachtsgeld oder Prämien gibt, hier nennen.
- **Trust-Punkte im Hero**: konkrete Fakten (Gründungsjahr, Teamgröße) wirken stärker.

Rechtliches ist verlinkt und bestätigt: [Impressum](https://vonbriel-maschinenbau.de/impressum)
und [Datenschutz](https://vonbriel-maschinenbau.de/datenschutz) (Footer + Consent-Checkbox
im Bewerbungsformular).

## GitHub Pages aktivieren

Settings → Pages → Source: „Deploy from a branch", Branch `main`, Ordner `/ (root)`.
Danach ist die Seite unter https://saviold.github.io/vonbriel/ erreichbar.
