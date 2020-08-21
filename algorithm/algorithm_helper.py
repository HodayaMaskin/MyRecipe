from db import db_init

def from_ingredients_to_binary(ingredients, ingredients_docs_count):
    bin_ing = [0] * (ingredients_docs_count + 1)
    for ing in ingredients:
        id = get_ingredient_id_by_name(ing['name'])
        bin_ing[id] = 1
    return bin_ing


def from_recipe_to_ingredients_binary(recipe, ingredients_docs_count):
    ingredients = recipe['ingredients']
    bin_ing = from_ingredients_to_binary(ingredients, ingredients_docs_count)
    return bin_ing


def get_ingredient_id_by_name(ingredient_name):
    collection = db_init.init_collection('ingredients')
    doc = collection.find_one({"name": ingredient_name})
    return doc['id']

# returns if all recipe ingredients are in the client ingredients list and the missed ingredients as array with 1 in each missed ingredient id
def ingredients_to_recipe_comparison(recipe, client_ingredients, ingredients_docs_count):
    recipe_ingredients = recipe['ingredients']
    bin_recipe = from_ingredients_to_binary(recipe_ingredients, ingredients_docs_count)
    bin_client = from_ingredients_to_binary(client_ingredients, ingredients_docs_count)
    # xor result will return the missed ingredients or the ingredients that the client have but do not appear in the recipe
    xor_result = xor_arrays(bin_recipe, bin_client)
    #check if xor result all filled by 0 -> client have all needed ingredients for recipe
    ingredients_equal = is_zero_array(xor_result)
    if(ingredients_equal):
        return True, xor_result
    # and result between the recipe and the xor will return only yhe ingredients that needed for recipe but the client missed
    and_result = and_arrays(bin_recipe, xor_result)
    return False, and_result


def xor_arrays(arr1, arr2):
    i = 0
    xor_result = [0] * 10
    for ing in arr1:
        xor_result[i] = ing ^ arr2[i]
        i = i + 1
    return xor_result


def and_arrays(arr1, arr2):
    i = 0
    and_result = [0] * 10
    for ing in arr1:
        and_result[i] = ing & arr2[i]
        i = i + 1
    return and_result


def is_zero_array(arr):
    for i in arr:
        if i != 0:
            return False
    return True
