__author__ = 'mmalca'
import json
#from urlparse import urlparse
#from urlparse import urlparse, parse_qs
from urllib.parse import urlparse,parse_qs


def get_ingredients_list(self):
    self.send_response(200)
    self.send_header('Access-Control-Allow-Origin', '*')
    self.send_header('Content-Type', 'application/json')
    self.end_headers()

    db_response = {
            "ingredients": [
                {
                    "_id": 1,
                    "name": "tomato"
                },
                {
                    "_id": 2,
                    "name": "oil"
                }
            ]
    }
    # json_string = json.dumps()
    self.wfile.write(json.dumps(db_response).encode('utf-8')) #on client side need to decode: json_from_server.decode('utf_8')
    print("sent json")

def get_recipe(self):
    ## need to get json: list of ids that represents the ingredients list from user
    #content_len = int(self.headers.get('Content-Length'))
    #json_ingredients_list = self.rfile.read(content_len) #Readin the data into json_ingredients_list (need to decode?)

    #### Option1:
    ##query = urlparse(self.path).query ## parsing the query of the GET request
    ##query_components = dict(qc.split("=") for qc in query.split("&"))
    ## imsi = query_components["imsi"] ## to pull a specific parameter named "imsi"

    #### Option2:
    query_components = parse_qs(urlparse(self.path).query)
    ingredients_from_user = query_components["ingredients"]
    print("received ingredients_list from user:")
    print(ingredients_from_user)


    ##ALGORITHM function: find a recipe: pull from db
    self.send_response(200)
    self.send_header('Access-Control-Allow-Origin', '*')
    self.send_header('Content-Type', 'application/json')
    self.end_headers()

    recipe = {
         "recipe_name": "Cake",
         "picture_url": "C:\pictures\1.jpg",
         "ingredients": [
                {
                    "_id": 1,
                    "name": "tomato",
                    "amount": "2 units"
                },
                {
                    "_id": 2,
                    "name": "oil",
                    "amount": "1 cup"
                }
         ],
         "DIRECTIONS": [
             "step 1",
             "step 2",
             "step 3"
            ]
    }

    self.wfile.write(json.dumps(recipe).encode('utf-8')) #on client side need to decode: json_from_server.decode('utf_8')
    print("sent json")

