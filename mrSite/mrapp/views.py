from django.shortcuts import render, redirect

# Create your views here.
import requests
from .forms import UserForm, addRecipesForm, addRecipesMing, RecipesDesc
from .templates.mrQueryTemplate.getTemplate import mrGetQuery, mrPostQuery

from .common import get_recipes, get_recipes_my, addUserToMr


def getPublicRecipes():
    recipes = requests.get(mrGetQuery.recipes.value).json()
    tmpList = []
    if recipes:
        for r in recipes:
            tmpList.append([recipes[r]['name'], recipes[r]['recipes_type'], recipes[r]['username']])
    return {"message": tmpList}


def index(request):
    if getPublicRecipes:
        return render(request, 'welcome.html', getPublicRecipes())
    else:
        return render(request, 'welcome.html', {"message": ""})


def recipes(request, recipes_name):
    steps_data = requests.get(mrGetQuery.recipesSteps.value % recipes_name).json()
    ming_data = requests.get(mrGetQuery.recipesMing.value % recipes_name).json()
    stepsData = []

    for s in steps_data:
        stepsData.append([steps_data[s]['step'], steps_data[s]['s_desc']])

    if str(request.user) == 'AnonymousUser':
        return render(request, 'recipes.html', {"stepsData": stepsData, "mingData": ming_data})
    else:
        return render(request, 'recipesLogged.html', {"stepsData": stepsData, "mingData": ming_data})


def userLogged(request):
    return render(request, 'userLogged.html', getPublicRecipes())


def myRecipes(request):
    return render(request, 'myRecipes.html', get_recipes_my(request.user))


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


stepsList = []
MingList = []


def newMing(MList):
    tmpMing = []
    for mgs in MList:
        tmpMing.append({"ming_id": mgs[0], "weight": mgs[1]})

    MingList.clear()
    return tmpMing


def prepareStepsJson(stepList):
    tmpSteps = []
    tmpSn = [sn for sn in range(1, len(stepList)+1)]
    for s, n in zip(stepList, tmpSn):
        tmp = {"s_num": n, "s_desc": s}
        tmpSteps.append(tmp)
    stepList.clear()

    return tmpSteps


def addRecipes(request):
    if request.method == "POST":
        form = addRecipesForm(request.POST)
        mingForm = addRecipesMing(request.POST)
        recipesDesc = RecipesDesc()
        print(request.POST)

        if recipesDesc.is_valid():
            pass

        if form.is_valid():
            if request.POST.get("addStep"):
                stepsList.append(form.cleaned_data["steps"])
            if request.POST.get("save"):
                prepareStepsJson(stepsList)

        if mingForm.is_valid():
            if request.POST.get("addIng"):
                MingList.append([mingForm.cleaned_data["ingredients"], mingForm.cleaned_data["weight"]])
                #newStep(form.cleaned_data["steps"])
            if request.POST.get("saveIng"):
                newMing(MingList)
                #prepareStepsJson(stepsList)
        #if form.is_valid():
            #if request.POST.get("save"):
                #print(request.POST.get())
        #newStesps(form.cleaned_data["steps"])
        #print(form.cleaned_data["steps"])

    else:
        form = addRecipesForm()
        mingForm = addRecipesMing()
        recipesDesc = RecipesDesc()

    return render(request, 'addRecipes.html', {"form": form, "stepsList": stepsList, "mingForm": mingForm, "MingList": MingList, "recipesDesc": recipesDesc })
