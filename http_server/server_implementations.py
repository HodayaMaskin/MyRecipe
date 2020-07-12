__author__ = 'mmalca'
import json


def get_ingredients_list(self):
    self.send_response(200)
    self.send_header('Access-Control-Allow-Origin', '*')
    self.send_header('Content-Type', 'application/json')
    self.end_headers()
    db_response = {
            "ingredients": [
            {
                        "name": "עגבניה",
                            "measurementUnit": "יחידות"
                    },
                    {
                            "name": "שמן",
                            "measurementUnit": "מל"
                    }
            ]
    }
    # json_string = json.dumps()
    self.wfile.write(json.dumps(db_response).encode('utf-8')) #on client side need to decode: json_from_server.decode('utf_8')
    print("sent json")