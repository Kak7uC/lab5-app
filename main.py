import time
import json
from http.server import BaseHTTPRequestHandler, HTTPServer

stats = {"count": 0}

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/time':
            stats["count"] += 1
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = {"time": int(time.time())}
            self.wfile.write(json.dumps(response).encode())
            
        elif self.path == '/metrics':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = {"count": stats["count"]}
            self.wfile.write(json.dumps(response).encode())
        
        else:
            self.send_response(404)
            self.end_headers()

if __name__ == "__main__":
    print("Server v2.0 started on port 8000...")
    server = HTTPServer(('0.0.0.0', 8000), Handler)
    server.serve_forever()
