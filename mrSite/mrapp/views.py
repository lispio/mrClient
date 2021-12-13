import json

from django.shortcuts import render

# Create your views here.
import requests
from django.http import HttpResponse
from json2html import *

from .templates.mrQueryTemplate.getTemplate import mrGetQuery


def index(request):

    recipes = requests.get(mrGetQuery.recipes.value).json()
    tmpList = []
    for r in recipes:
        tmpList.append([recipes[r]['name'], recipes[r]['recipes_type'], recipes[r]['username']])

    return render(request, 'welcome.html', {"message": tmpList})


def recipes(request, recipes_name):
    steps_data = requests.get(mrGetQuery.recipesSteps.value % recipes_name).json()
    ming_data = requests.get(mrGetQuery.recipesMing.value % recipes_name).json()
    stepsData = []

    for s in steps_data:
        stepsData.append([steps_data[s]['step'], steps_data[s]['s_desc']])

    return render(request, 'recipes.html', {"stepsData": stepsData, "mingData": ming_data})
