from db.db_init import init_collection
##import pymongo


def get_ingredients_list():
    ## myclient = pymongo.MongoClient("mongodb://193.106.55.98:5000/")
    ## mydb = myclient["RecipeForMe"]
    ## ingredientsCollection = mydb["ingredients"]
    ingredients_collection = init_collection("ingredients")
    ingredients_list = ingredients_collection.find()
    return ingredients_list

def get_recipes_list():
    recipes_collection = init_collection("ingredients")
    recipes_list = recipes_collection.find()
    return recipes_list

## not needed
def add_ingredients(ingredients_list):
    # myclient = pymongo.MongoClient("mongodb://193.106.55.98:5000/")
    # mydb = myclient["RecipeForMe"]
    # ingredientsCollection = mydb["ingredients"]
    ingredients_collection = init_collection("ingredients")

    ingredients_collection.insert_many(ingredients_list)

    documents = ingredients_collection.find()
    for x in documents:
        print(x)

def add_ingredients_from_recipe(recipe):
    #Create a dictionary and add to the Collection
    ##TO: for each ingredient in list: if does not exist: add to

    ingredients = init_collection("ingredients")

    for recipe_ing in recipe['ingredients']:
        ##print(recipe_ing)
        if ingredients.find_one({"name":recipe_ing}) == None:
            #this is a new ingredient, add to ingredients collection:
            ingredients.insert({"_id":get_next_sequence_value("ingredientid"),
                                "name":recipe_ing,
                                "vector":"4"#fast text op,
                                })
    # for each recipe_ing in Recipe.ingredients:
        # for each ing in collection(ingredients list)
        # if recipe_ing._id != ing._id and it is the last ing in collection(ingredients list):save
            #create new id if needed!! id =
            # check vector using fast text ft_vector = []
            # ingredient_dictionary = { _id = id## check the id how to append a new one
                                        # "name" : recipe_ing.name,
                                        #"vector" : ft_vector []
                                        # }
                                     ###{ "name": "John", "address": "Highway 37" }



    # ingredient_to_add = collection.insert_one(ingredient_dictionary)

    ##y = mycol.find_one()

#returns the next sequence for the increasing counter (sequence_name=ingredientid)
def get_next_sequence_value(collection_name, sequence_name):
    collection = init_collection(collection_name)
    sequence_document = collection.find_and_modify(
        query = {'_id': sequence_name },
        update = {"$inc":{'sequence_value':1}},
        new = 'true' ##?
    )
    return sequence_document.sequence_value

    ##### TO USE WHEN INSERTING INGREDIENT: #####
    #.insert({"_id":get_next_sequence_value("ingredientid"),
    #       "name": ....
    #       ...})