from db import db_init

def from_ingredients_to_binary(ingredients, ingredientsCount):
    buckets = [0] * ingredientsCount
    for ing in ingredients:
        id = get_ingredient_id_by_name("בצל")

def get_ingredient_id_by_name(ingredient_name):
    collection = db_init.init_collection('ingredients')
    doc = collection.find_one({ "name": ingredient_name })
    return doc['id']