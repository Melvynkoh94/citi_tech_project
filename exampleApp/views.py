from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm, SnippetForm, UserForm_extended
from .CitiTech_BuyerClass import *
#from .CitiTech_BuyerClass_Final import *
from .HouseDatabaseGenerator import *
from .push_notification import *

user_num = 500

# Create views here
def home(request):
  return render(request, 'exampleApp/home.html')


def about(request):
  return render(request, 'exampleApp/about.html')


def form(request):
  user_num=500
  user_num+=1
  if(user_num>500):
    alert_many_users(user_num)

  #If this is a POST request then process the Form data
  if (request.method == 'POST'):
    form = UserForm(request.POST) #create a UserForm instance and populate it with data from the request (binding)
    # Check if he form is valid
    if form.is_valid():
      push_notification()
      ##########################
      #if(user_num>100):
        #push_notification()

      ##########################
      request.session['web_input'] = request.POST['web_input']

      age = form.cleaned_data['age']
      gender = form.data['gender']
      monthlyIncome = form.cleaned_data['monthlyIncome']
      essentialExpenses = form.cleaned_data['essentialExpenses']
      personalSavings = form.cleaned_data['personalSavings']
      availDownPay = form.cleaned_data['availDownPay']
      existingLoan = form.cleaned_data['existingLoan']
      locations = form.cleaned_data['locations']

      buyer = Buyer(age, gender, monthlyIncome, essentialExpenses, personalSavings, availDownPay, existingLoan, locations)
      maxAffordability = buyer.priceCeiling()
      maxAffordability += 20000

      print()
      print('The amount you are estimated to be able to afford is:' + "{0:,}".format(maxAffordability))
      shownHousingList = displayHomes(maxAffordability)
      print('Housing List: '+ str(shownHousingList))
      print()

      print('from views.form: VALID')
      print(age, gender, monthlyIncome, essentialExpenses, personalSavings, essentialExpenses, personalSavings, availDownPay, existingLoan, locations) #just to check on the console if this works
  form = UserForm()
  return render(request, 'exampleApp/form.html', {'form': form})

def form_extended(request):
  ##########################
  url = request.session.get('web_input')
  if request.method == 'POST':
    print('In views.form_extended')
    form_extended = UserForm_extended(request.POST)
    if form_extended.is_valid():
      y1 = form_extended.cleaned_data['y1']
      y2 = form_extended.cleaned_data['y2']
      y3 = form_extended.cleaned_data['y3']

      print('y1: '+y1)
      print('y2: '+y2)
      print('y3: '+y3)    
      print('VALID')

      form_extended.save()
  
  form_extended = UserForm_extended() 
  return render(request, 'exampleApp/form_extended.html', {'form_extended': form_extended})

def houseView(request):
  url = request.session.get('web_input')
  if request.method == 'POST':
    form_extended = UserForm_extended(request.POST)
    if form_extended.is_valid():
      y1 = form_extended.cleaned_data['y1']
      y2 = form_extended.cleaned_data['y2']
      y3 = form_extended.cleaned_data['y3']

      print('y1: '+y1)
      print('y2: '+y2)
      print('y3: '+y3)    
      print('VALID')

      form_extended.save()
  
  form_extended = UserForm_extended() 
  return render(request, 'exampleApp/house1.html', {'form_extended': form_extended})

def houseView2(request):
  url = request.session.get('web_input')
  if request.method == 'POST':
    form_extended = UserForm_extended(request.POST)
    if form_extended.is_valid():
      y1 = form_extended.cleaned_data['y1']
      y2 = form_extended.cleaned_data['y2']
      y3 = form_extended.cleaned_data['y3']

      print('y1: '+y1)
      print('y2: '+y2)
      print('y3: '+y3)    
      print('VALID')

      form_extended.save()
  
  form_extended = UserForm_extended() 
  return render(request, 'exampleApp/house2.html', {'form_extended': form_extended})

def houseView3(request):
  url = request.session.get('web_input')
  if request.method == 'POST':
    form_extended = UserForm_extended(request.POST)
    if form_extended.is_valid():
      y1 = form_extended.cleaned_data['y1']
      y2 = form_extended.cleaned_data['y2']
      y3 = form_extended.cleaned_data['y3']

      print('y1: '+y1)
      print('y2: '+y2)
      print('y3: '+y3)    
      print('VALID')

      form_extended.save()
  
  form_extended = UserForm_extended() 
  return render(request, 'exampleApp/house3.html', {'form_extended': form_extended})

     


def snippets(request):
  if request.method == 'POST':
    form = SnippetForm(request.POST)
    if form.is_valid():
      print('VALID')
      form.save()
  form = SnippetForm()
  return render(request, 'exampleApp/form.html', {'form': form})


 
