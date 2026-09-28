# Instagram-Assets · Wilfried von Briel Maschinenbau

Profilbild, Highlight-Cover und Bio für das Instagram-Profil. Gebaut wie die
Facebook-Assets: HTML/CSS in [`index.html`](index.html), gerendert mit
`python3 render.py` nach [`png/`](png). Gleiche Farben, gleiche Schrift, gleiches
Logo wie Karriereseite und Ad-Creatives.

**Instagram hat kein Titelbild.** Statt eines Pendants zum Facebook-Titelbild
prägen dort das Profilbild, die Highlight-Cover und die ersten Feed-Posts den
Auftritt – genau die liegen hier.

## Die Dateien

| Datei | Format | Verwendung |
|---|---|---|
| `png/profilbild-monogramm.png` | 1080 × 1080 | **Empfehlung** als Profilbild |
| `png/profilbild.png` | 1080 × 1080 | Alternative mit vollständigem Logo |
| `png/highlight-jobs.png` | 1080 × 1080 | Cover für das Highlight „Jobs" |
| `png/highlight-team.png` | 1080 × 1080 | Cover für „Team" |
| `png/highlight-werkstatt.png` | 1080 × 1080 | Cover für „Werkstatt" |
| `png/highlight-kontakt.png` | 1080 × 1080 | Cover für „Kontakt" |

Alles wird von Instagram **rund** zugeschnitten – die Motive sind deshalb mittig
aufgebaut, mit Abstand zum Rand. Das Profilbild erscheint im Feed nur rund 32 px
groß; deshalb die Empfehlung fürs Monogramm, dessen Form auch dort trägt. Die
Highlight-Cover tragen nur ein Symbol: die Beschriftung setzt Instagram selbst
unter den Kreis, ein Wort im Bild wäre doppelt.

## Feed und Stories

Dafür braucht es nichts Neues – die Ad-Creatives passen direkt:

- **Feed-Posts:** `creatives/png/*-45.png` (1080 × 1350, das 4:5-Format, das im
  Feed am meisten Fläche bekommt)
- **Stories und Reels:** `creatives/png/*-story.png` (1080 × 1920)

## Bio (max. 150 Zeichen)

Instagram erlaubt deutlich weniger als Facebook: **150 Zeichen** in der Bio und
**30 Zeichen** im Namensfeld. Alle Varianten sind gezählt (Emojis zählen doppelt).

**Namensfeld** – das fettgedruckte Feld, nach dem Instagram auch sucht:

- `von Briel Maschinenbau` (22 Zeichen) – Empfehlung
- `von Briel Maschinenbau | Jobs` (29 Zeichen) – während der Kampagne

**Variante A – Recruiting (147 Zeichen)**

> Maschinen- & Anlagenbau am Bodensee. Montage, Elektromontage, Verdrahtung.
> Aktuell gesucht: Industrieelektriker (m/w/d) – bewirb dich in 60 Sek. 👇

**Variante B – Unternehmen, dauerhaft (134 Zeichen)**

> Wilfried von Briel Maschinenbau · Allensbach am Bodensee.
> Montage & Elektromontage von Maschinen und Anlagen. Handwerk, das man sieht.

**Variante C – Team im Mittelpunkt (138 Zeichen)**

> Maschinenbau am Bodensee. Ein Team, das zusammenhält – und Platz für einen
> Elektriker mehr. Offene Stelle & Einblicke aus der Werkstatt 👇

Das 👇 in A und C zeigt auf den Link darunter – nur sinnvoll, wenn dort auch die
Karriereseite verlinkt ist.

## Einrichten

1. **Profil zu einem Unternehmensprofil machen** (Einstellungen → Kontotyp).
   Erst dann lässt sich das Konto mit dem Meta-Werbekonto verbinden und die
   Anzeigen laufen sauber auf beiden Plattformen.
2. **Profilbild:** `profilbild-monogramm.png` hochladen, Zuschnitt nicht
   verschieben – das Bild ist quadratisch und mittig aufgebaut.
3. **Name und Bio** aus den Varianten oben einsetzen.
4. **Link:** während der Kampagne die Karriereseite, sonst
   `vonbriel-maschinenbau.de`.
5. **Highlights anlegen:** je ein Highlight „Jobs", „Team", „Werkstatt",
   „Kontakt" erstellen und das passende Cover als Bild wählen. Instagram
   verlangt für ein Highlight mindestens eine Story – zur Not eine Story posten,
   archivieren und dann ins Highlight legen.

## Ändern und neu rendern

Symbole und Beschriftungen stehen im `ASSETS`-Array in `index.html`. Nach
Änderungen `python3 render.py` ausführen (Playwright mit Chromium nötig).
