# Ad-Creatives · Industrieelektriker (m/w/d)

Recruiting-Motive für Meta in zwei Formaten – **Feed 4:5 (1080×1350)** und
**Story/Reels 9:16 (1080×1920)**. Gebaut als HTML/CSS in [`index.html`](index.html)
und als PNG gerendert nach [`png/`](png). Farben, Wortmarke und Schrift kommen
aus derselben CI wie die Karriereseite.

## Die fünf Konzepte

Bewusst kein „Wir suchen …": jedes Motiv spricht entweder die Qualifikation an
(und filtert damit schon in der Anzeige vor) oder den Bewerbungsaufwand.

| Konzept | Idee | Foto nötig |
|---|---|---|
| `fehlt-hier-was` | Stromlaufplan mit **offener Klemme** → „Fehlt hier was? Genau: du." | nein |
| `l2-farbe` | Insider-Frage in echten Aderfarben → „Du weißt, welche Farbe L2 hat?" | nein |
| `team-daumen` | Team-Foto → „Drei Daumen hoch. Einer fehlt noch." | `team.jpg` |
| `kein-band-kein-buero` | Arbeitsplatz-Foto + die drei Voraussetzungen als Haken | `elektromontage.jpg` |
| `kaffeepause` | Anti-Aufwand fürs Retargeting → „Deine Bewerbung passt in eine Kaffeepause." | `kollege-ok.jpg` |

**Ohne Foto** greift automatisch die Schaltplan-Variante – die PNGs im Ordner
sind also nie leer, aber `team-daumen` und `kaffeepause` entfalten ihre Wirkung
erst mit Bild. Sofort schaltbar sind `fehlt-hier-was` und `l2-farbe`.

## Fotos ergänzen und neu rendern

1. Die Dateien nach `../assets/` legen (dieselben wie auf der Karriereseite):
   `team.jpg`, `elektromontage.jpg`, `kollege-ok.jpg` – Landscape, längste
   Kante ca. 2000 px.
2. `python3 render.py` ausführen → die PNGs in `png/` werden überschrieben.

Voraussetzung fürs Rendern: `pip install playwright && playwright install chromium`.
Ist Chromium schon im System, findet das Script es selbst (oder per
`CHROMIUM_PATH=/pfad/zu/chrome python3 render.py`).

## Texte ändern oder neue Stelle ergänzen

Alles liegt im `CONCEPTS`-Array in `index.html`. Ein Eintrag erzeugt automatisch
beide Formate. Für eine weitere Stelle einfach das `JOB`-Objekt kopieren bzw.
Konzepte mit eigenen Texten anlegen und neu rendern. `index.html` im Browser
öffnen zeigt alle Motive als verkleinerte Vorschau.

## Gestaltungsregeln, die eingebaut sind

- **Story-Safe-Zone:** oben 280 px, unten 330 px bleiben frei – dort liegt in
  Stories die Meta-Oberfläche (Profilzeile, Antwortfeld).
- **Landscape-Fotos** sitzen im 9:16-Format immer oben statt vollflächig, damit
  der Zuschnitt nicht ins Bild hineinzoomt und Köpfe abschneidet.
- **Kein Text unter dem Foto-Rand:** Headline und CTA starten unterhalb der
  Bildkante, der Verlauf endet in genau der Farbe der Fläche darunter (keine
  sichtbare Naht).
- **Prüfung im Render:** Headline, CTA und Wortmarke liegen in jedem der zehn
  Motive vollständig innerhalb der Fläche.
