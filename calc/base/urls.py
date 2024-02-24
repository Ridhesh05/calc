
from django.contrib import admin
from django.urls import path

from . import views
urlpatterns = [
   
    path('', views.main,name='main'),
    path('calculate/',views.calculate,name='calculate'),
]
