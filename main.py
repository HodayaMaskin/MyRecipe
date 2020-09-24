from algorithm import algorithm
from db import db_operations
##algorithm.choose_recipe([1, 2,3,4,5,6,7,8,10])

    ###  Adding new recipe ####


from db import db_operations
name = "עוגה במילוי טחינה ואגוזים"
ingredients = [{"name":"ביצה","amount" :"2"}, {"name":"סוכר","amount" :"שליש כוס"}, {"name":"שמן","amount" :"שליש כוס"},{"name":"תמצית וניל","amount" :"חצי כפית"}, {"name":"מיץ תפוזים","amount" :"חצי כוס"}, {"name":"קמח","amount" :"כוס"},{"name":"סודה לשתיה","amount" :"רבע כפית"}, {"name":"טחינה","amount" :"2 כפות"}, {"name":"דבש","amount" :"כף"}, {"name":"אגוז מלך","amount" :"2 כפות"}]
directions = ["מחממים תנור מראש ל-180 מעלות ומשמנים תבנית אינגליש קייק.", "מערבבים בקערית 2 כפות טחינה גולמית עם כף מלאה דבש/מייפל ומניחים בצד.", "מערבבים בקערה (בעזרת מטרפה ידנית או מיקסר) את הביצים עם הסוכר. מוסיפים שמן, תמצית וניל ומיץ ומערבבים. מוסיפים קמח תופח ואבקת סודה לשתיה ומערבבים קלות עד לאיחוד חומרים.", "יוצקים ¾ מהבלילה לתבנית משומנת. מוסיפים את תערובת הטחינה והדבש ומפזרים אגוזים טחונים. יוצקים מעל את יתר הבלילה (הבלילה לא אמורה לכסות את כל המילוי) ומערבבים קלות עם סכין (כמו שמערבבים עוגת שיש).", "מכניסים לתנור החם ואופים במשך כ-30 דקות, עד שקיסם יוצא יבש."]

db_operations.add_recipe(name,ingredients , directions, "jpg")

    ########### test - printing the recipe that we have inserted:

from db import db_init
collection = db_init.init_collection('recipes')
myquery = { "name":name}
mydoc = collection.find(myquery)
for doc in mydoc:
    id = doc["_id"]
    print(doc)

    ########### test - print new ingredirnts list
ingredients_list = db_operations.get_ingredients_list()
print("new ingredients list (only names and ids): ---------------")
for i in ingredients_list:
    print(i)
