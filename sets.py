from sets_categories_data import (ALCOHOLS)

def clean_ingredients(dish_name, dish_ingredients):
    dish_ingredients1 = set(dish_ingredients)
    return dish_name, dish_ingredients1

from sets_categories_data import ALCOHOLS
def check_drinks(drink_name, drink_ingredients):
    drink_ingredients1 = set(drink_ingredients)
    if len(drink_ingredients1.intersection(ALCOHOLS))>0:
        return f"{drink_name} Cocktail"
    else:
        return f"{drink_name} Mocktail"
