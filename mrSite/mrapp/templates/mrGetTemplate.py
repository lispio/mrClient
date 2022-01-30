from enum import Enum

from .configModule import mrConfig


class mrGetQuery(Enum):
    recipes = f"http://{mrConfig.mrHost.value}:{mrConfig.mrPort.value}/recipes"
    recipesMy = f"http://{mrConfig.mrHost.value}:{mrConfig.mrPort.value}/my_recipes?username=%s"
    recipesSteps = f"http://{mrConfig.mrHost.value}:{mrConfig.mrPort.value}/recipes_steps?recipesName=%s"
    recipesMing = f"http://{mrConfig.mrHost.value}:{mrConfig.mrPort.value}/recipes_ming?recipesName=%s"
    ingredients = f"http://{mrConfig.mrHost.value}:{mrConfig.mrPort.value}/get_ingredients"


class mrPostQuery(Enum):
    addUser = f"http://{mrConfig.mrHost.value}:{mrConfig.mrPort.value}/add_user/"
    addRecipes = f"http://{mrConfig.mrHost.value}:{mrConfig.mrPort.value}/add_recipes"
