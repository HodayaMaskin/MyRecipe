##import pymongo
## from http_server.server_init import init_server
#from http_server import JsonOperations ##import *
from fast_test_operations.first_impression import first_try
from db import db_operations ## import *

# my tries to serialize / deserialize from/to json
# j = '{"action": "print", "method": "onData", "data": "Madan Mohan"}'
#p = JsonToObject(j)

#r = Recipe('hodaya', 123)
#m = r.ObjectToJson()
#print(m)
# end of json tests

##first_try()
#Connect to the DB
#myclient = pymongo.MongoClient("mongodb://193.106.55.98:5000/")
#GetIngredients()
#init_server()
from db import db_init
collection = db_init.init_collection('recipes')
dict=collection.find_one({"name":"תבשיל שעועית ואפונה"})
##for recipe_ing in dict['ingredients']:
  ##  print(recipe_ing)

from db import db_operations
#db_operations.add_ingredients_from_recipe(dict)

col =  db_init.init_collection('counters')
#col.insert({"_id":get_next_sequence_value("ingredientid"),
                #    "name":recipe_ing})