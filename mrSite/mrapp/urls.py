from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('recipes/<str:recipes_name>', views.recipes),
]
