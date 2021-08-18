import http.server
import socketserver
import sqlite3

#import urllib3
#handler = http.server.SimpleHTTPRequestHandler
#with socketserver.TCPServer(("", 1234), handler) as httpd:
#   httpd.serve_forever()
#http = urllib3.PoolManager()
#from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
#class HttpProcessor(BaseHTTPRequestHandler):
conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()
cursor.execute("""CREATE TABLE albums (data text)""")
class MyServer(http.server.SimpleHTTPRequestHandler):
 def do_POST(self):
  length = int(self.headers['content-length'])
  body = self.rfile.read(length)
  self.send_response(200)
  body_dec=body.decode('utf-8')
  html_file=open('index.html','a')
  html_file.write(body_dec)
  self.end_headers()
  html_file.close()
  message = """INSERT INTO albums VALUES ('{a}')"""
  message2=message.format(a=body_dec)
  print(body_dec)
  cursor.execute(message2)
  conn.commit()
  return body_dec
httpd = socketserver.TCPServer(('', 1234), MyServer)
httpd.serve_forever()
print(body_dec)
