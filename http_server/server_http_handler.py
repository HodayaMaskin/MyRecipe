__author__ = 'mmalca'

from http_server.server_implementations import *

from http.server import BaseHTTPRequestHandler
class http_handler(BaseHTTPRequestHandler): ## This class inherits from BaseHTTPRequestHandler

    def do_GET(self):

        print(self.path.partition('?'))
        if self.path == '/getAvailableIngredients':
            get_ingredients_list(self)

        if self.path.startswith("/getRecipe"):
            get_recipe(self)