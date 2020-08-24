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

from db import db_operations
#db_operations.add_ingredients_from_recipe(dict)

#col =  db_init.init_collection('counters')
#col.insert({"_id":get_next_sequence_value("ingredientid"),
                #    "name":recipe_ing})


######################################################################################################

    #### DON'T ERASE - Adding new recipe ####
#from db import db_operations
#ingredients = [{"name": "שוקולד מריר", "amount": "200 גרם"}, {"name": "שמנת מתוקה", "amount":"500 מל"}]
# directions = ["שוברים את השוקולד לקוביות ושמים בקערה.", "מוסיפים לקערה 250 מל שמנת מתוקה וממיסים יחד במיקרוגל או על בן מארי, עד שהתערובת אחידה.", "מצננים את תערובת השוקולד במקרר במשך 2-3 שעות לפחות, או עד שהיא קרה לגמרי.", "מעבירים את תערובת השוקולד הקרה לקערת מיקסר ומוסיפים פנימה את יתרת השמנת.", "מקציפים יחד במהירות גבוהה עד שמתקבל מוס אחיד ומעט רך.", "מעבירים את המוס לשק זילוף וממלאים את הכוסות עד ל-2/3 מגובהן.", "מקשטים בשוקולד קצוץ ומגישים."]
#
# db_operations.add_recipe("מוס שוקולד",ingredients , directions, "jpg")

    ############ test - printing the recipe that we have inserted:

# from db import db_init
# collection = db_init.init_collection('recipes')
# myquery = { "name":"מוס שוקולד"}
# mydoc = collection.find(myquery)
# for doc in mydoc:
#     id = doc["_id"]
#     print(doc)

    ########### fixing specific element of our recipe if needed

# from db import db_init
# collection = db_init.init_collection('recipes')
# myquery = { "name":"עוגת כדורי שוקולד"}
# mydoc = collection.find(myquery)
# for doc in mydoc:
#     id = id = doc["_id"]
    ##to_update_pic = "C:\pictures\\" + str(id) + ".jpg"
    ##to_update_ing = [{"name":"","amount" :""}, {"name":"","amount" :""}, {"name":"","amount" :""},{"name":"","amount" :""}, {"name":"","amount" :""}, {"name":"","amount" :""},{"name":"","amount" :""}, {"name":"","amount" :""}, {"name":"","amount" :""}]
    ##to_update_ing = [{"name":"בצל","amount" :"1"}, {"name":"שום","amount" :"2-3 שיניים"}, {"name":"אפונה","amount" :"2 כוסות"},{"name":"","amount" :""}, {"name":"שעועית ירוקה","amount" :"3 כוסות"}, {"name":"","amount" :""},{"name":"מים","amount" :"שליש כוס"}, {"name":"מלח","amount" :"חצי כפית"}, {"name":"כורכום","amount" :"רבע כפית"},{"name":"אבקת מרק","amount" :"כפית"},{"name":"פלפל שחור","amount" :"מעט"}]
    # to_update_ing = [{"name":"ביסקוויט","amount" :"400 גרם"},
    #  {"name":"שמנת מתוקה","amount" :"375 מל"},
    #  {"name":"שוקולד מריר","amount" :"200 גרם"}]

    # updated = collection.find_one_and_update(
    #         {"_id" : id},
    #         {"$set":
    #             {"ingredients": to_update_ing}
    #
    #         },upsert=True
    #     )

        ################# print all recipes

# from db import db_init
# collection = db_init.init_collection('recipes')
# docs = collection.find()
# for doc in docs:
#     print(doc)
#     print()
#     print("=======================")
#     print()

######################################################################################################
