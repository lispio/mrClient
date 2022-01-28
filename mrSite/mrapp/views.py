import json
from django import forms
from django.shortcuts import render, redirect

# Create your views here.
import requests
from .forms import UserForm, addRecipesForm, addRecipesMing, RecipesDesc, recipesPreviewForm
from .templates.mrQueryTemplate.getTemplate import mrGetQuery, mrPostQuery

from .common import get_recipes, get_recipes_my, addUserToMr, get_ingredients


stepsList = []
mingList = []
desc = []
recipesInfo = []
tmpMing = []

geI = None
geM = None
geS = None

jsonMing = None
jsonSteps = None
jsonInfo = None


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


def newMing(MList):
    for mgs in MList:
        tmpMing.append({"ming_id": mgs[0], "weight": mgs[1], "name": mgs[2]})
    MList.clear()
    return tmpMing


def getRecipesType(rtype):
    rt = None
    if rtype in ['1', 'bread', 'chleb']:
        rt = 1
    elif rtype in ['2', 'cheese', 'ser']:
        rt = 2
    elif rtype in ['3', 'wine', 'wino']:
        rt = 3
    elif rtype in ['4', 'liquor', 'nalewka']:
        rt = 4

    return rt


def recipesIsPublic(info):
    if info is None:
        IsPublic = False
    else:
        IsPublic = True
    return IsPublic


def addDesc(Info, userid):
    recInfo = {"name": Info[0][0],
               "user_id": userid,
               "recipes_type": getRecipesType(Info[0][1]),
               "is_public": recipesIsPublic(Info[0][3]),
               "des": Info[0][2], }
    return recInfo


def prepareStepsJson(stepList):
    tmpSteps = []
    tmpSn = [sn for sn in range(1, len(stepList) + 1)]
    for s, n in zip(stepList, tmpSn):
        tmp = {"s_num": n, "s_desc": s}
        tmpSteps.append(tmp)
    stepList.clear()
    return tmpSteps


def prepareAddRecipesJson(jI, jM, jS):
    if jI:
        global geI
        geI = jI
    if jM:
        global geM
        geM = jM
    if jS:
        global geS
        geS = jS

    if geI and geM and geS:
        recpiesJson = geI
        recpiesJson["steps"] = geS
        recpiesJson["ming"] = geM
        geI = None
        geS = None
        geM = None
        return recpiesJson


ing = dict(get_ingredients())


def addIngredients(request):
    global jsonMing
    if request.method == "POST":
        mingForm = addRecipesMing(request.POST)
        if mingForm.is_valid():
            if request.POST.get("addIng"):
                mingList.append([mingForm.cleaned_data['ingredients'], mingForm.cleaned_data["weight"],
                                 ing[int(mingForm.cleaned_data['ingredients'])]])
            if request.POST.get("saveIng"):
                jsonMing = newMing(mingList)
                mingList.clear()
    else:
        if jsonMing:
            jsonMing.clear()
        mingForm = addRecipesMing()
    return render(request, "addIngredients.html", {"mingForm": mingForm, "MingList": mingList})


def addSteps(request):
    global jsonSteps
    if request.method == "POST":
        form = addRecipesForm(request.POST)

        if form.is_valid():
            if request.POST.get("addStep"):
                stepsList.append(form.cleaned_data["steps"])
            if request.POST.get("save"):
                jsonSteps = prepareStepsJson(stepsList)
                stepsList.clear()
    else:
        if jsonSteps:
            jsonSteps.clear()
        form = addRecipesForm()

    return render(request, 'addSteps.html', {"form": form, "stepsList": stepsList})


def recipesPreview(request):
    print("JI")
    print(jsonInfo)
    print("JM")
    print(jsonMing)
    print("JS")
    print(jsonSteps)
    if request.method == "POST":
        form = recipesPreviewForm(request.POST)
        if form.is_valid():
            if request.POST.get('saveRecipes'):
                rec = prepareAddRecipesJson(jsonInfo, jsonMing, jsonSteps)
                response = requests.post(mrPostQuery.addRecipes.value, data=json.dumps(rec))
                print(response)
    else:
        form = recipesPreviewForm()
    return render(request, 'recipesPreview.html', {"form": form, "jsonInfo": jsonInfo, "jsonMing": jsonMing, "jsonSteps": jsonSteps})


def addRecipes(request):
    global jsonInfo
    if request.method == "POST":
        recipesDesc = RecipesDesc()

        if request.POST.get('saveDes'):
            recipesInfo.append([request.POST.get('recipesName'),
                                request.POST.get('recipesType'),
                                request.POST.get('recipesDesc'),
                                request.POST.get('is_public')])

            jsonInfo = addDesc(recipesInfo, request.user.id)
            recipesInfo.clear()
    else:
        if jsonInfo:
            jsonInfo.clear()
        recipesDesc = RecipesDesc()

    return render(request, 'addRecipes.html', {"recipesDesc": recipesDesc})
