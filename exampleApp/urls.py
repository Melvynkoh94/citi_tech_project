from django.contrib import admin
from django.urls import path
from . import views #import our views.py

##REFER TO:https://matthiasomisore.com/web-programming/display-image-in-a-django-template-using-imagefield/
#from . import settings
#from django.contrib.staticfiles.urls import static
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('',views.home, name='exampleApp-home'), #name is just the name of the path
    #pattern for the route is empty ''. means localhost:8000/exampleApp/'' in urls.py in citi_tech
    path('about/', views.about, name='exampleApp-home'),
    path('form/', views.form, name='exampleApp-home'),
    path('form_extended/', views.form_extended, name='exampleApp-home'),
    path('snippets/', views.snippets, name='exampleApp-home'),
    path('about/form', views.form, name='exampleApp-home'),
    path('form_extended/house1/', views.houseView, name='exampleApp-home'),
    path('form_extended/house2/', views.houseView2, name='exampleApp-home'),
    path('form_extended/house3/', views.houseView3, name='exampleApp-home'),
] 

