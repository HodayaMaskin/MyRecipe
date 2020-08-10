from db.db_init import init_collection
##import pymongo

products = [
#{ "name": "rice" },
#{ "name": "oil" },
]

def get_ingredients():
    # myclient = pymongo.MongoClient("mongodb://193.106.55.98:5000/")
    # mydb = myclient["RecipeForMe"]
    # ingredientsCollection = mydb["ingredients"]
    ingredientsCollection = init_collection("ingredients")

    documents = ingredientsCollection.find()
    for x in documents:
        print(x)

def add_ingredients():
    # myclient = pymongo.MongoClient("mongodb://193.106.55.98:5000/")
    # mydb = myclient["RecipeForMe"]
    # ingredientsCollection = mydb["ingredients"]
    ingredientsCollection = init_collection("ingredients")

    ingredientsCollection.insert_many(products)

    documents = ingredientsCollection.find()
    for x in documents:
        print(x)

def add_ingredients_from_recipe(recipe):
    #Create a dictionary and add to the Collection
    ##TO: for each ingredient in list: if does not exist: add to

    collection = init_collection("ingredients")


    # for each recipe_ing in Recipe.ingredients:
        # for each ing in collection(ingredients list)
        # if recipe_ing._id != ing._id and it is the last ing in collection(ingredients list):
            #create new id if needed!! id =
            # check vector using fast text ft_vector = []
            # ingredient_dictionary = { _id = id## check the id how to append a new one
                                        # "name" : recipe_ing.name,
                                        #"vector" : ft_vector []
                                        # }
                                     ###{ "name": "John", "address": "Highway 37" }



    # ingredient_to_add = collection.insert_one(ingredient_dictionary)

    ##y = mycol.find_one()