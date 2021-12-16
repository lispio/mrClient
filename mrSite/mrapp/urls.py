from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', include("django.contrib.auth.urls")),
    path('recipes/<str:recipes_name>', views.recipes, name="recipes"),
    path('signup', views.signup, name="signup"),
    path('userLogged', views.userLogged, name="userLogged"),
    path('addRecipes', views.addRecipes, name="addRecipes"),
    path('myRecipes', views.myRecipes, name="myRecipes"),
]
