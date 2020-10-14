from algorithm import algorithm
from db import db_operations
# rec = algorithm.choose_recipe([1, 2,3,4,5,6,7,8,10])
# for r in rec:
#      print(r)


from db import db_init
collection = db_init.init_collection('recipes')


docs = collection.find()
for doc in docs:
    print(doc)
    print()
    print("=======================")
    print()

    ###  Adding new recipe ####


# from db import
# db_operations
# name = "ריבועי שוקולד לבן וקוקוס"
#
# ingredients = [
# {"name":"שוקולד לבן","amount" :"100 גרם"},
# {"name":"שמן","amount" :"רבע כוס"},
# {"name":"ביצה","amount" :"2"},
# {"name":"סוכר","amount" :"2 כפות"},
#
# {"name":"קמח שקדים","amount" :"שליש כוס"},
# {"name":"קוקוס","amount" :"שליש כוס"},
# {"name":"פודינג","amount" :"כף"}
# ]
#
#
#
# directions = ["מחממים תנור ל-170 מעלות.","מניחים בקערית את קוביות השוקולד הלבן והשמן וממיסים מספר שניות במיקרוגל. מוציאים ומערבבים עד לתערובת חלקה. מצננים מעט.",
#     "מערבבים במטרפה או בכף (אין צורך במיקסר) את הביצים עם הסוכר. מוסיפים את תערובת השוקולד ומערבבים.",
#               "מוסיפים קמח שקדים וקוקוס ומערבבים לתערובת אחידה.",
#               "יוצקים לתבנית משומנת ואופים בתנור במשך 27-30 דקות, עד שקיסם יוצא יבש.",
#     "מוציאים מהתנור ומניחים לזה להתקרר. חותכים לריבועים קטנים. שומרים בקופסה סגורה על השיש."
# ]
# db_operations.add_recipe(name,ingredients , directions, "jpg")

print("================")
#
#     ########### test - printing the recipe that we have inserted:
#



# from db import db_init
# collection = db_init.init_collection('recipes')
# #myquery = { "name":name}
# mydoc = collection.find()#(myquery)
# i =0
# for doc in mydoc:
#     #id = doc["_id"]
#     print(doc)
#     print()
#     print("----   recipe number  {}    ----------------".format(i))
#     print()
#     i+=1

#
#     ########### test - print new ingredirnts list
# ingredients_list = db_operations.get_ingredients_list()
# print("new ingredients list (only names and ids): ---------------")
# for i in ingredients_list:
#     print(i)

