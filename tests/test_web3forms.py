"""Prueft die Web3Forms-Anbindung der Karriereseite.

Aufruf:  python3 tests/test_web3forms.py   (Playwright mit Chromium noetig)

Startet einen lokalen Server auf dem Repo, faengt api.web3forms.com ab und
spielt drei Faelle durch: Erfolg mit Anhang, abgelehnter Anhang, Totalausfall.
"""
import http.server
import socketserver
import threading
import pathlib
import sys
import tempfile
from playwright.sync_api import sync_playwright

ROOT = pathlib.Path(__file__).resolve().parent.parent
PORT = 8841
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
KEY = "b2edd9f9-850d-4dfa-80d1-3a1b2d01d07e"

CV = pathlib.Path(tempfile.gettempdir()) / "lebenslauf-test.pdf"
CV.write_bytes(b"%PDF-1.4\n% Testdatei fuer den Upload\n")

fehler = []
SRV = None


def check(bedingung, text):
    print(("  OK   " if bedingung else "  FEHL ") + text)
    if not bedingung:
        fehler.append(text)


class Quiet(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **kw):
        super().__init__(*a, directory=str(ROOT), **kw)

    def log_message(self, *a):
        pass


def serve():
    socketserver.ThreadingTCPServer.allow_reuse_address = True
    srv = socketserver.ThreadingTCPServer(("127.0.0.1", PORT), Quiet)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    return srv


def durchlauf(page, antworten):
    """Beantwortet die Fragen der Reihe nach mit dem angegebenen Index."""
    for i, wahl in enumerate(antworten):
        page.wait_for_selector("#opts .option")
        page.locator("#opts .option").nth(wahl).click()
        page.wait_for_timeout(260)


def formular(page, mit_datei):
    page.wait_for_selector("#fName")
    page.fill("#fName", "Max Mustermann")
    page.fill("#fPhone", "0170 1234567")
    page.fill("#fPlz", "78476")
    page.locator("details.more summary").click()
    page.fill("#fEmail", "max@example.com")
    if mit_datei:
        page.set_input_files("#fCv", str(CV))
    page.check("#fConsent")
    page.click("#submitBtn")


def lauf(szenario, antwort_fn, mit_datei=True):
    """Spielt einen Durchlauf und liefert Anfragen + Zustand der Erfolgsseite.

    Achtung: page.content() enthaelt auch den Quelltext des Inline-Scripts –
    eine Textsuche darin findet Markup, das gar nicht gerendert wurde. Deshalb
    wird hier ueber Selektoren gezaehlt, nicht im HTML gesucht.
    """
    print(f"\n=== {szenario} ===")
    anfragen, gescheitert = [], []
    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path=CHROME)
        page = browser.new_page()
        # HEAD-Anfragen sind die Existenzpruefung der optionalen Fotos:
        # Die Antwort kommt an (200) und wird danach verworfen, Chromium
        # meldet das als ERR_ABORTED. Kein Fehler der Seite.
        page.on("requestfailed",
                lambda r: gescheitert.append(r.url) if r.method != "HEAD" else None)

        def web3(route, request):
            anfragen.append({
                "method": request.method,
                "headers": request.headers,
                "body": request.post_data or "",
            })
            antwort_fn(route, len(anfragen))

        page.route("**/api.web3forms.com/**", web3)
        page.route("**/api-v2.lead-table.com/**",
                   lambda route, req: route.fulfill(status=200, body="{}"))

        page.goto(f"http://127.0.0.1:{PORT}/index.html")
        durchlauf(page, [0, 0, 0, 0])
        formular(page, mit_datei)
        page.wait_for_timeout(1800)
        zustand = {
            "erfolg": page.locator(".success").count(),
            "cv_hinweis": page.locator(".success__cv").count(),
            "fehler": page.locator("#formError.is-visible").count(),
            "fehlertext": (page.locator("#formError").inner_text()
                           if page.locator("#formError").count() else ""),
            "mailto": page.locator('a[href^="mailto:"]').count(),
            "gescheitert": gescheitert,
        }
        browser.close()
    return anfragen, zustand


SRV = serve()

# ---------------------------------------------------------------- Fall 1
anfragen, z = lauf(
    "Fall 1: Anhang geht durch",
    lambda route, n: route.fulfill(
        status=200, content_type="application/json",
        body='{"success":true,"message":"Email sent successfully"}'),
)
check(len(anfragen) == 1, f"genau ein POST an Web3Forms (war: {len(anfragen)})")
if anfragen:
    r = anfragen[0]
    ct = r["headers"].get("content-type", "")
    body = r["body"]
    check(r["method"] == "POST", "Methode POST")
    check(ct.startswith("multipart/form-data; boundary="),
          f"multipart mit Boundary vom Browser (war: {ct[:40]})")
    check(KEY in body, "access_key ist im Body")
    check('name="access_key"' in body, "Feldname access_key")
    check('name="subject"' in body and "Bewerbung Industrieelektriker" in body,
          "Betreff mit Stelle")
    check("Max Mustermann" in body, "Name im Betreff/Body")
    check('name="from_name"' in body, "from_name gesetzt")
    check('name="replyto"' in body and "max@example.com" in body,
          "replyto auf die Bewerber-Adresse")
    check('name="attachment"' in body and "lebenslauf-test.pdf" in body,
          "Anhang als Feld 'attachment' mit Dateiname")
    check('name="Frage: Ausbildung"' in body, "Antwort Ausbildung im Body")
    check('name="Frage: Schaltplan"' in body, "Antwort Schaltplan im Body")
    check('name="Frage: Deutschkenntnisse"' in body, "Antwort Deutsch im Body")
    check('name="Qualifikation"' in body, "Qualifikation im Body")
    check('name="Quelle"' in body, "Quelle im Body")
    check("_subject" not in body and "_template" not in body,
          "keine formsubmit-Altlasten (_subject/_template)")
check(z["erfolg"] == 1, "Erfolgsseite erscheint")
eigene = [u for u in z["gescheitert"] if "analytics." not in u]
check(not eigene, f"alle Dateien der Seite laden ({eigene})")
check(z["cv_hinweis"] == 0,
      "kein Hinweis zum Nachreichen (der Lebenslauf kam ja an)")

# ---------------------------------------------------------------- Fall 2
def abgelehnt(route, n):
    if n == 1:
        route.fulfill(status=422, content_type="application/json",
                      body='{"success":false,"message":"File type not allowed"}')
    else:
        route.fulfill(status=200, content_type="application/json",
                      body='{"success":true,"message":"Email sent successfully"}')


anfragen, z = lauf("Fall 2: Anhang wird abgelehnt", abgelehnt)
check(len(anfragen) == 2, f"zweiter Versuch ohne Anhang (Anfragen: {len(anfragen)})")
if len(anfragen) == 2:
    check('name="attachment"' in anfragen[0]["body"], "erster Versuch mit Anhang")
    check('name="attachment"' not in anfragen[1]["body"],
          "zweiter Versuch ohne Anhang")
    check("Max Mustermann" in anfragen[1]["body"],
          "zweiter Versuch enthaelt weiterhin alle Daten")
check(z["erfolg"] == 1 and z["cv_hinweis"] == 1,
      "Erfolgsseite weist auf das Nachreichen des Lebenslaufs hin")

# ---------------------------------------------------------------- Fall 3
anfragen, z = lauf(
    "Fall 3: Web3Forms nicht erreichbar",
    lambda route, n: route.abort(),
)
check(z["fehler"] == 1 and "nicht geklappt" in z["fehlertext"], "Fehlermeldung erscheint")
check(z["mailto"] >= 1, "Mailto-Ausweg wird angeboten")

# ---------------------------------------------------------------- Fall 4
# KO-Antwort: es darf gar nichts rausgehen - weder Mail noch LeadTable.
print("\n=== Fall 4: KO-Antwort sendet nichts ===")
web3, leadtable = [], []
with sync_playwright() as p:
    browser = p.chromium.launch(executable_path=CHROME)
    page = browser.new_page()
    page.route("**/api.web3forms.com/**",
               lambda r, q: (web3.append(q.url),
                             r.fulfill(status=200, body='{"success":true}')))
    page.route("**/api-v2.lead-table.com/**",
               lambda r, q: (leadtable.append(q.url),
                             r.fulfill(status=200, body="{}")))
    page.goto(f"http://127.0.0.1:{PORT}/index.html")
    page.wait_for_selector("#opts .option")
    page.locator("#opts .option").last.click()  # „Nein" = KO
    page.wait_for_timeout(900)
    absage = page.locator(".reject__ic, .reject__soft").count()
    text = page.locator("#funnelBody").inner_text()
    browser.close()
check(not web3, f"keine E-Mail bei KO (Anfragen: {len(web3)})")
check(not leadtable, f"kein LeadTable-Lead bei KO (Anfragen: {len(leadtable)})")
check(absage >= 1 or "leider" in text.lower(), "Absage-Screen erscheint")

# ---------------------------------------------------------------- Ergebnis
print("\n" + "=" * 52)
if fehler:
    print(f"{len(fehler)} FEHLER:")
    for f in fehler:
        print("  -", f)
    sys.exit(1)
print("Alles gruen.")
