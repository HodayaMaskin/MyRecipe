__author__ = 'mmalca'


def init_server():
    PORT = 80
    #IP =
    #server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
    server = HTTPServer(('10.10.248.98', PORT), http_handler)
    print('Server is running on port %s'%PORT)
    server.serve_forever()
