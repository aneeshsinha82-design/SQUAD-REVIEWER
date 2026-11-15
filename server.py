"""Minimal local server for the FC Mobile Squad Finder."""
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse, parse_qs
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent

class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def do_GET(self):
        parsed = urlparse(self.path)
        if parsed.path == "/api/squad":
            uid = parse_qs(parsed.query).get("uid", [""])[0].strip()
            if not uid:
                return self.send_json(400, {"error": "A UID is required."})
            return self.send_json(501, {
                "error": "Live squad lookup is not configured.",
                "detail": "The site is running, but no verified public FC Mobile UID-to-squad endpoint has been integrated. No squad data was invented."
            })
        if parsed.path == "/":
            self.path = "/index.html"
        return super().do_GET()

    def send_json(self, status, data):
        body = json.dumps(data).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

if __name__ == "__main__":
    print("FC Mobile Squad Finder running at http://localhost:8000")
    print("Press Ctrl+C to stop.")
    ThreadingHTTPServer(("127.0.0.1", 8000), Handler).serve_forever()
