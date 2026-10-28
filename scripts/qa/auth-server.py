from http.server import SimpleHTTPRequestHandler,ThreadingHTTPServer
from urllib.parse import urlsplit
import os
from pathlib import Path
os.chdir(Path(__file__).resolve().parents[2]/'dist')
class Handler(SimpleHTTPRequestHandler):
 def do_GET(self):
  if urlsplit(self.path).path=='/__test_login':
   self.send_response(302);self.send_header('Set-Cookie','qa_session=ok; Path=/; SameSite=Lax; HttpOnly');self.send_header('Location','/');self.end_headers();return
  if 'qa_session=ok' not in self.headers.get('Cookie',''):
   self.send_response(401);self.send_header('Content-Type','text/html');self.end_headers();self.wfile.write(b'Login required');return
  return super().do_GET()
 def log_message(self,*args):pass
server=ThreadingHTTPServer(('127.0.0.1',0),Handler)
print(f'http://127.0.0.1:{server.server_port}',flush=True)
server.serve_forever()
