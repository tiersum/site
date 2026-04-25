#!/usr/bin/env python3
"""Local dev server for tiersum-site with SPA fallback."""

import argparse
import http.server
import os
import socketserver

DEFAULT_PORT = 8000


class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        path = self.path

        # SPA fallback: /site/* without .md → index.html
        if path.startswith('/site/') and not path.endswith('.md'):
            self.path = '/index.html'
        elif path == '/':
            self.path = '/index.html'

        return super().do_GET()

    def log_message(self, fmt, *args):
        print(f"[{self.log_date_time_string()}] {args[0]} {args[1]} - {args[2]}")


if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    parser = argparse.ArgumentParser(description="Local dev server for tiersum-site")
    parser.add_argument("port", nargs="?", type=int, default=None,
                        help=f"Port to listen on (default: {DEFAULT_PORT})")
    args = parser.parse_args()

    port = args.port or int(os.environ.get("PORT", DEFAULT_PORT))

    with socketserver.TCPServer(("", port), Handler) as httpd:
        print(f"Serving tiersum-site at http://localhost:{port}")
        print("Press Ctrl+C to stop")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")
