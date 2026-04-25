#!/usr/bin/env python3
"""Local dev server for tiersum-site with SPA fallback."""

import argparse
import http.server
import os
import socketserver

DEFAULT_PORT = 8000

# Friendly page for /ui/ paths when backend is not running
UI_STUB_HTML = """<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Management UI — TierSum</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        html, body { background-color: #020617; color: #cbd5e1; }
    </style>
</head>
<body class="min-h-screen flex items-center justify-center p-4">
    <div class="max-w-md w-full bg-slate-900/50 border border-slate-800 rounded-xl p-8 text-center">
        <div class="w-16 h-16 bg-blue-500/10 rounded-full flex items-center justify-center mx-auto mb-6">
            <svg class="w-8 h-8 text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z"/>
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/>
            </svg>
        </div>
        <h1 class="text-xl font-bold text-slate-100 mb-2">Management UI</h1>
        <p class="text-slate-400 mb-6">
            The management interface is served by the <strong class="text-blue-400">tiersum</strong> Go backend.
            It is not available in local static-site mode.
        </p>
        <div class="bg-slate-800/50 rounded-lg p-4 text-left text-sm font-mono text-slate-300 mb-6">
            <p class="text-slate-500 mb-1"># Start the backend (in tiersum repo)</p>
            <p>go run cmd/main.go</p>
        </div>
        <a href="/" class="btn btn-primary btn-sm inline-flex items-center gap-2 px-4 py-2 bg-blue-600 hover:bg-blue-500 text-white rounded-lg transition-colors">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"/>
            </svg>
            Back to Site
        </a>
    </div>
</body>
</html>"""


class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        path = self.path

        # Management UI paths — show friendly stub when backend is not running
        if path.startswith('/ui/'):
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(UI_STUB_HTML.encode('utf-8'))
            return

        # SPA fallback: /site/* without .md → index.html
        if path.startswith('/site/') and not path.endswith('.md'):
            self.path = '/index.html'
        elif path == '/':
            self.path = '/index.html'

        try:
            return super().do_GET()
        except FileNotFoundError:
            self.send_response(404)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(b"<h1>404 Not Found</h1>")

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
