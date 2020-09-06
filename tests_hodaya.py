__author__ = 'mmalca'

import fasttext
import fasttext.util

#fasttext.util.download_model('he', if_exists='ignore')
#ft_he = fasttext.load_model('cc.he.300.bin')

#     ####  Adding new recipe ####
#
from db import db_operations
def myfunc():
    ingredients = [{"name": "בצל", "amount": "1"}, {"name": "קישוא", "amount":"3"}, {"name": "מלח", "amount":"חצי כפית"}, {"name": "כורכום", "amount":"רבע כפית"}, {"name": "פלפל שחור", "amount":"קמצוץ"}]
    directions = ["מחממים מחבת רחבה (רצוי מחבת עם ציפוי שאינו נדבק) עם 2 כפות שמן זית ומטגנים את הבצל עד להזהבה.", "חותכים את הקישואים לקוביות","מוסיפים את הקישואים, ממליחים מעט עם המלחייה ומערבבים. מכסים ומבשלים על אש בינונית-נמוכה במשך 10-12 דקות, עד שהקישואים מתרככים אבל לא לגמרי." , "מרימים את המכסה ומתבלים במלח, כורכום ופלפל שחור. מערבבים ומבשלים על אש בינונית (ללא מכסה) במשך 5 דקות עד שהקישואים מזהיבים (במידה והתערובת מתייבשת במחבת אפשר להוסיף 2-3 כפות מים). טועמים ומתקנים תיבול לפי הצורך."]
#
    #db_operations.add_recipe("סלט קישואים מבושל",ingredients , directions, "jpg")
#
#     ########### test - printing the recipe that we have inserted:
#
    from db import db_init
    collection = db_init.init_collection('recipes')
#myquery = { "name":"סלט ירקות בסיסי"}

    listofrecipes = collection.find()
    for doc in listofrecipes:
        id = doc["_id"]
        print(doc)

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



####### Hodaya's test

# import pymongo
# mongo_server = pymongo.MongoClient("mongodb://193.106.55.98:5000/")
# from algorithm import algorithm_helper
# id = algorithm_helper.get_ingredient_id_by_name("בצל")
#
# collection = db_init.init_collection('recipes')
# recipe = collection.find_one()
# print(recipe)
#
# collection = db_init.init_collection('ingredients')
# #doc = collection.find_one({ "name": "בצל" })
# items_in_ing_col_count = collection.count_documents({})
# bin1 = algorithm_helper.from_recipe_to_ingredients_binary(recipe, items_in_ing_col_count)
# bin = algorithm_helper.from_ingredients_to_binary(recipe['ingredients'], items_in_ing_col_count)
# print(bin)

