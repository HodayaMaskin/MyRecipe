__author__ = 'mmalca'

from http_server.server_implementations import *

from http.server import BaseHTTPRequestHandler

class http_handler(BaseHTTPRequestHandler): ## This class inherits from BaseHTTPRequestHandler

    def do_GET(self):
        if self.path == '/getAvailableIngredients':
            get_ingredients_list(self)