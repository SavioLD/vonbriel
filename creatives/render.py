#!/usr/bin/env python3
"""Rendert die Ad-Creatives aus index.html als PNG nach png/.

Aufruf:  python3 render.py
Voraussetzung: playwright + Chromium (pip install playwright && playwright install chromium)

Jedes Motiv in index.html hat ein data-name – daraus wird der Dateiname.
Fehlende Fotos unter ../assets/ sind kein Problem: die Motive fallen dann auf
die Typo-/Schaltplan-Variante zurück (siehe index.html).
"""
import functools
import glob
import http.server
import os
import pathlib
import socketserver
import threading

from playwright.sync_api import sync_playwright

ROOT = pathlib.Path(__file__).resolve().parent.parent  # Repo-Wurzel
OUT = pathlib.Path(__file__).resolve().parent / "png"
PORT = 8811


def chromium_path():
    """Nimmt CHROMIUM_PATH, sonst ein vorhandenes Chromium aus dem System.
    Gibt None zurück, dann sucht Playwright selbst."""
    env = os.environ.get("CHROMIUM_PATH")
    if env and pathlib.Path(env).exists():
        return env
    muster = [
        "/opt/pw-browsers/chromium-*/chrome-linux/chrome",
        os.path.expanduser("~/.cache/ms-playwright/chromium-*/chrome-linux/chrome"),
        "/usr/bin/chromium",
        "/usr/bin/chromium-browser",
        "/usr/bin/google-chrome",
    ]
    for m in muster:
        treffer = sorted(glob.glob(m))
        if treffer:
            return treffer[-1]
    return None


class Server(socketserver.TCPServer):
    allow_reuse_address = True  # sonst blockiert TIME_WAIT den nächsten Lauf

    def handle_error(self, request, client_address):
        pass  # abgebrochene Requests nicht als Traceback ausgeben


def serve():
    """Kleiner lokaler Server – file:// blockiert Schriften und HEAD-Checks.
    Ist der Port belegt, wird der nächste freie genommen."""
    handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(ROOT))
    for port in range(PORT, PORT + 20):
        try:
            httpd = Server(("127.0.0.1", port), handler)
        except OSError:
            continue
        threading.Thread(target=httpd.serve_forever, daemon=True).start()
        return httpd, port
    raise SystemExit("Kein freier Port zwischen %d und %d gefunden." % (PORT, PORT + 19))


def main():
    OUT.mkdir(exist_ok=True)
    httpd, port = serve()
    try:
        with sync_playwright() as pw:
            exe = chromium_path()
            browser = pw.chromium.launch(executable_path=exe) if exe else pw.chromium.launch()
            page = browser.new_page(viewport={"width": 1200, "height": 2000}, device_scale_factor=1)
            page.goto(f"http://127.0.0.1:{port}/creatives/index.html?render=1")
            page.wait_for_timeout(400)
            page.evaluate("document.fonts.ready")
            page.wait_for_timeout(600)
            canvases = page.locator(".canvas")
            n = canvases.count()
            for i in range(n):
                el = canvases.nth(i)
                name = el.get_attribute("data-name")
                el.screenshot(path=str(OUT / f"{name}.png"))
                print(f"  {name}.png")
            print(f"{n} Motive in {OUT}")
            browser.close()
    finally:
        httpd.shutdown()


if __name__ == "__main__":
    main()
