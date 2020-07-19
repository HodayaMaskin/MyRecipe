import pymongo

products = [
{ "name": "rice" },
{ "name": "oil" },
{ "name": "red wine" }
]

def add_ingredients():
    myclient = pymongo.MongoClient("mongodb://193.106.55.98:5000/")
    mydb = myclient["RecipeForMe"]
    ingredientsCollection = mydb["ingredients"]
    ingredientsCollection.insert_many(products)

    documents = ingredientsCollection.find()
    for x in documents:
        print(x)
