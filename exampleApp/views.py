from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
  #return HttpResponse('<h1>Citi Tech Homepage</h1>')
  return render(request, 'exampleApp/home.html')

def about(request):
  #return HttpResponse('<h1>Citi Tech About</h1>')
  return render(request, 'exampleApp/about.html')

 
