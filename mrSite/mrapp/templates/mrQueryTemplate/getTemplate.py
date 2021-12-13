from enum import Enum


class mrGetQuery(Enum):
    recipes = "http://127.0.0.1:7979/recipes"
    recipesSteps = "http://127.0.0.1:7979/recipes_steps?recipesName=%s"
    recipesMing = "http://127.0.0.1:7979/recipes_ming?recipesName=%s"
