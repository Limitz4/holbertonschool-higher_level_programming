#!/usr/bin/python3
import json
from http.server import HTTPServer, BaseHTTPRequestHandler

class H(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/': self.r(200, 'text/plain', 'Hello, this is a simple API!')
        elif self.path == '/data': self.r(200, 'application/json', {"name": "John", "age": 30, "city": "New York"})
        elif self.path == '/status': self.r(200, 'text/plain', 'OK')
        elif self.path == '/info': self.r(200, 'application/json', {"version": "1.0", "description": "A simple API built with http.server"})
        else: self.r(404, 'text/plain', 'Endpoint not found')
    
    def r(self, code, ctype, data):
        self.send_response(code)
        self.send_header('Content-type', ctype)
        self.end_headers()
        if isinstance(data, dict): data = json.dumps(data)
        self.wfile.write(data.encode() if isinstance(data, str) else data)

if __name__ == "__main__":
    HTTPServer(('', 8000), H).serve_forever()
