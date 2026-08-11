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
