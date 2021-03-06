import requests

from .templates.mrGetTemplate import mrGetQuery, mrPostQuery


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
        return {"myRecipes": tmpMyRecipes}
    else:
        return {"myRecipes": ""}


def get_ingredients():
    ingredients = requests.get(mrGetQuery.ingredients.value).json()
    tmpIng = []
    for ing in ingredients:
        tmpIng.append((ingredients[ing]['id'], ingredients[ing]['name']))

    return tmpIng


def addUserToMr(username):
    requests.post(mrPostQuery.addUser.value, data='{"name": "%s"}' % username)
    return {"message": "added"}
