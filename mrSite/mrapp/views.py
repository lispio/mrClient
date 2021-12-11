import json

from django.shortcuts import render

# Create your views here.
import requests
from django.http import HttpResponse
from json2html import *


def index(request):
    recipes = requests.get("http://127.0.0.1:7979/recipes").json()
    conntext = {}
    tmpList = []
    for r in recipes:
        conntext.update({recipes[r]['name']: recipes[r]['recipes_type']})
        tmpList.append([recipes[r]['name'], recipes[r]['recipes_type'], recipes[r]['username']])
    return render(request, 'recipes.html', {"tmpList": tmpList})
    #return render(request, 'recipes.html', {"recipes": conntext})

