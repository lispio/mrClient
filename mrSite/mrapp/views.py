from django.shortcuts import render, redirect

# Create your views here.
import requests
from .forms import UserForm
from .templates.mrQueryTemplate.getTemplate import mrGetQuery, mrPostQuery

from .common import get_recipes, get_recipes_my, addUserToMr


def index(request):
    recipes = requests.get(mrGetQuery.recipes.value).json()
    tmpList = []
    if recipes:
        for r in recipes:
            tmpList.append([recipes[r]['name'], recipes[r]['recipes_type'], recipes[r]['username']])

        return render(request, 'welcome.html', {"message": tmpList})
    else:
        return render(request, 'welcome.html', {"message": ""})


def recipes(request, recipes_name):
    steps_data = requests.get(mrGetQuery.recipesSteps.value % recipes_name).json()
    ming_data = requests.get(mrGetQuery.recipesMing.value % recipes_name).json()
    stepsData = []

    for s in steps_data:
        stepsData.append([steps_data[s]['step'], steps_data[s]['s_desc']])

    return render(request, 'recipes.html', {"stepsData": stepsData, "mingData": ming_data})


def userLogged(request):
    return render(request, 'userLogged.html', get_recipes_my(request.user))


def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            addUserToMr(form.cleaned_data.get("username"))
            return redirect('login')
    else:
        form = UserForm()
    return render(request, 'signup.html', {'form': form})


