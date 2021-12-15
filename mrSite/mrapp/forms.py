from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class UserForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class addRecipesForm(forms.Form):
    steps = forms.CharField(max_length=250)


class addRecipesMing(forms.Form):
    ingredients = forms.CharField(max_length=250)
    weight = forms.CharField(label="weight (g) ", max_length=5)


class RecipesDesc(forms.Form):
    recipesName = forms.CharField(label="Recipes Name", max_length=50)
    recipesType = forms.CharField(label="Recipes Type")
    is_public = forms.BooleanField(required=False)
    recipesDesc = forms.CharField(label="Recipes Desc", max_length=200)
    #"name": "Wheat Bread-Everyday",
    #"user_id": 1,
    #"recipes_type": 1,
    #"is_public": true,
    #"des": "simple bright bread on yeast",

