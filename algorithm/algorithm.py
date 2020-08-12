__author__ = 'mmalca'

from algorithm import algorithm_support_functions
from db import db_operations
### CORE ALGORITHM FUNCTION ###

def choose_recipe(ingredients_from_user):
    ## access to the ingredients list from db
    ingredients_list = db_operations.get_ingredients_list()
    ## access to recipes list in db
    recipes_list = db_operations.get_recipes_list()

    for recipe in recipes_list:
        for recipe_ingredient in recipe.ingredients:
            for user_ingredient in ingredients_from_user:
                if recipe_ingredient._id != user_ingredient._id and recipe_ingredient._id:

    # checking vector distance between ingredients and setting score to recipe

    ###

    ## send to user back, using http_server functions
    print() ## to delete after