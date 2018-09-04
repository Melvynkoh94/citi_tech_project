from django.contrib import admin
from django.urls import path

from . import views #import our views.py

urlpatterns = [
    path('',views.home, name='exampleApp-home'), #name is just the name of the path
    #pattern for the route is empty ''. means localhost:8000/exampleApp/'' in urls.py in citi_tech
    path('about/', views.about, name='exampleApp-home')
] 