import json

from django.shortcuts import render

# Create your views here.
import requests
from django.http import HttpResponse
from json2html import *


def index(request):

    recipes = requests.get("http://127.0.0.1:7979/recipes").json()
    tmpList = []
    for r in recipes:
        tmpList.append([recipes[r]['name'], recipes[r]['recipes_type'], recipes[r]['username']])

    return render(request, 'welcome.html', {"message": tmpList})


def recipes(request, recipes_name):
    recipes_data = requests.get("http://127.0.0.1:7979/recipes_steps?recipesName=%s" % recipes_name).json()
    print(recipes_data)
    data = {"data": recipes_data}
    return render(request, 'recipes.html', data)
