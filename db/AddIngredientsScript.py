import pymongo

products = [
#{ "name": "rice" },
#{ "name": "oil" },
#{ "name": "red wine" },
#{ "name": "salt" },
#{ "name": "pepper" },
#{ "name": "noodles" },
#{ "name": "water" },
#{ "name": "potato" },
#{ "name": "tomato" },
#{ "name": "eggplant" },
#{ "name": "zucchini" },
#{ "name": "cucumber" },
#{ "name": "onion" },
#{ "name": "chicken breast" },
#{ "name": "Tuna" },
#{ "name": "Been" },
#{ "name": "Hummus" },
#{ "name": "egg" }
]

def GetIngredients():
    myclient = pymongo.MongoClient("mongodb://193.106.55.98:5000/")
    mydb = myclient["RecipeForMe"]
    ingredientsCollection = mydb["ingredients"]
    documents = ingredientsCollection.find()
    for x in documents:
        print(x)

def add_ingredients():
    myclient = pymongo.MongoClient("mongodb://193.106.55.98:5000/")
    mydb = myclient["RecipeForMe"]
    ingredientsCollection = mydb["ingredients"]
    ingredientsCollection.insert_many(products)

    documents = ingredientsCollection.find()
    for x in documents:
        print(x)