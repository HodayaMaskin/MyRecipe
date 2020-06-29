__author__ = 'mmalca'

def get_ingredients_list(self):
    self.send_response(200)
    #self.send_header('Content-Type', 'application/json')
    #self.end_headers()
    json_string = json.dumps({
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
    })
    self.wfile.write(json_string)
