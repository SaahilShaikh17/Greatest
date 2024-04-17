from http.server import BaseHTTPRequestHandler, HTTPServer

HOST = 'localhost'
PORT = 8000

class MyHandler(BaseHTTPRequestHandler):
  """Handles incoming HTTP requests."""

  def do_GET(self):
    """Responds to GET requests."""
    self.send_response(200)
    self.send_header('Content-type', 'text/html')
    self.end_headers()
    message = "<h1>Hello, world!</h1>"
    self.wfile.write(message.encode())

with HTTPServer((HOST, PORT), MyHandler) as server:
  print(f"Server listening on http://{HOST}:{PORT}")
  server.serve_forever()