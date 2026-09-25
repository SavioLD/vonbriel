# Facebook-Assets · Wilfried von Briel Maschinenbau

Profilbild, Titelbild und Bio für die Facebook-Seite. Gebaut wie die Ad-Creatives:
HTML/CSS in [`index.html`](index.html), gerendert mit `python3 render.py` nach
[`png/`](png). Farben, Schrift und Logo kommen aus derselben Quelle wie die
Karriereseite – Profil- und Titelbild passen dadurch zueinander.

## Die Dateien

| Datei | Format | Verwendung |
|---|---|---|
| `png/profilbild-monogramm.png` | 1000 × 1000 | **Empfehlung** als Profilbild |
| `png/profilbild.png` | 1000 × 1000 | Alternative mit dem vollständigen Logo |
| `png/titelbild-firma.png` | 1640 × 720 | Titelbild, dauerhaft nutzbar |
| `png/titelbild-stelle.png` | 1640 × 720 | Titelbild für die Zeit der Stellenanzeige |

### Warum zwei Profilbilder?

Facebook zeigt das Profilbild **rund** und je nach Stelle nur 40–60 px groß
(im Feed, unter Kommentaren). Das vollständige Logo hat zwei Textzeilen, die
bei dieser Größe zu einem grauen Streifen verschwimmen. Das **Monogramm**
bleibt erkennbar – deshalb die Empfehlung. Beide Varianten sind aus derselben
Logodatei aufgebaut, nichts wurde nachgezeichnet oder umgefärbt.

### Warum 1640 × 720 beim Titelbild?

Das ist 820 × 360 in doppelter Auflösung – Facebook rechnet herunter und das
Bild bleibt auf Retina-Displays scharf. Beim Aufbau sind drei Zonen beachtet,
die Facebook unterschiedlich beschneidet:

- **Handy** zeigt nur die mittleren ~1280 px der Breite → Text und Logo liegen
  innerhalb dieses Bereichs.
- **Desktop** zeigt 820 × 312 statt 360 → oben und unten bleiben je ~48 px frei.
- **Unten links** schiebt sich am Desktop das Profilbild über das Titelbild →
  dieser Bereich bleibt textfrei.

Der Render prüft diese drei Zonen bei jedem Durchlauf.

## Bio (max. 255 Zeichen)

**Variante A – Unternehmen + offene Stelle (235 Zeichen)**

> Maschinen- und Anlagenbau in Allensbach am Bodensee. Wir montieren und verdrahten Maschinen – im Team, mit Handwerk und Erfahrung. Aktuell verstärken wir die Elektromontage: Industrieelektriker (m/w/d) gesucht. vonbriel-maschinenbau.de

**Variante B – Unternehmen, dauerhaft (213 Zeichen)**

> Wilfried von Briel Maschinenbau in Allensbach am Bodensee: Montage, Elektromontage und Verdrahtung von Maschinen und Anlagen. Kurze Wege, erfahrene Kollegen, saubere Arbeit. Mehr über uns: vonbriel-maschinenbau.de

**Variante C – Recruiting-Fokus (230 Zeichen)**

> Maschinenbau am Bodensee – und ein Team, das zusammenhält. In Allensbach montieren und verdrahten wir Maschinen und Anlagen. Du bist Elektriker und liest Schaltpläne sicher? Dann sprich uns an: Industrieelektriker (m/w/d) gesucht.

Für die Kampagnenzeit passt A (Titelbild `titelbild-stelle`), danach B mit dem
Titelbild `titelbild-firma`.

## Einrichten

1. **Profilbild:** Seite → Bearbeiten → Profilbild → `profilbild-monogramm.png`.
   Facebook bietet beim Hochladen einen Zuschnitt an – dort nichts verschieben,
   das Bild ist bereits quadratisch und mittig aufgebaut.
2. **Titelbild:** Titelbild ändern → `titelbild-stelle.png` (oder `-firma`).
   Beim Repositionieren nur bei Bedarf minimal vertikal schieben.
3. **Bio:** Info → Beschreibung/Bio → eine der drei Varianten einfügen.
4. **Link:** `vonbriel-maschinenbau.de` als Website hinterlegen; für die Kampagne
   zusätzlich die Karriereseite als Button „Jetzt bewerben" verlinken.

## Ändern und neu rendern

Texte stehen im `ASSETS`-Array in `index.html`, die Firmendaten im `FIRMA`-Objekt.
Nach Änderungen `python3 render.py` ausführen – Voraussetzung ist Playwright mit
Chromium (`pip install playwright && playwright install chromium`), ein bereits
installiertes Chromium findet das Script selbst.
