import requests

from .templates.mrQueryTemplate.getTemplate import mrGetQuery


def get_recipes():
    recipes = requests.get(mrGetQuery.recipes.value).json()
    tmpList = []
    if recipes:
        for r in recipes:
            tmpList.append([recipes[r]['name'], recipes[r]['recipes_type'], recipes[r]['username']])

        return {"message": tmpList}
    else:
        return {"message": ""}


def get_recipes_my(username):
    myRecipes = requests.get(mrGetQuery.recipesMy.value % username).json()

    if myRecipes:
        tmpMyRecipes = []
        for myR in myRecipes:
            tmpMyRecipes.append([myRecipes[myR]['name'], myRecipes[myR]['recipes_type'], myRecipes[myR]['username']])

        return {"message": tmpMyRecipes}
    else:
        return {"message": ""}
