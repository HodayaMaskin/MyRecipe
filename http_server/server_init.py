__author__ = 'mmalca'

from http.server import BaseHTTPRequestHandler, HTTPServer
import json

from http_server.server_http_handler import *

def init_server():
    PORT = 80
    #IP =
    #server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
    server = HTTPServer(('10.10.248.98', PORT), http_handler)
    print('Server is running on port %s'%PORT)
    server.serve_forever()

init_server()