import time
import json
from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/time':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = {"time": int(time.time())}
            self.wfile.write(json.dumps(response).encode())

if __name__ == "__main__":
    server = HTTPServer(('0.0.0.0', 8000), Handler)
    print("Server started on port 8000...")
    server.serve_forever()