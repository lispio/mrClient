from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .common import get_ingredients


class UserForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class addRecipesForm(forms.Form):
    steps = forms.CharField(max_length=250)


class addRecipesMing(forms.Form):
    ingredients = forms.CharField(label='ingredients:', widget=forms.Select(choices=get_ingredients()))
    weight = forms.CharField(label="weight (g) ", max_length=5)


class RecipesDesc(forms.Form):
    REC_TYPE_CHOICES = [(1, 'chleb'), (2, 'ser'), (3, 'wino')]
    IS_PUBLIC = [(1, True), (2, False), (3, 'Protected')]
    recipesName = forms.CharField(label="Recipes Name", max_length=50)
    recipesType = forms.CharField(label="Recipes Type", widget=forms.Select(choices=REC_TYPE_CHOICES))
    is_public = forms.BooleanField(required=False, widget=forms.Select(choices=IS_PUBLIC))
    recipesDesc = forms.CharField(label="Recipes Desc", max_length=200)


class recipesPreviewForm(forms.Form):
    pass
