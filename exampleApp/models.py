from django.db import models
from multiselectfield import MultiSelectField
from .choices import *

class Snippet(models.Model):
  #name = models.CharField(max_length=100)
  #email = models.EmailField(max_length=100)
  age = models.IntegerField(null=True)
  gender  = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')  
  #REFER TO https://docs.djangoproject.com/en/dev/ref/models/fields/#field-choices
  
  monthlyIncome = models.PositiveIntegerField(null=True)
  essentialExpenses = models.PositiveIntegerField(null=True)
  personalSavings = models.PositiveIntegerField(null=True)
  availDownPay = models.PositiveIntegerField(null=True)
  existingLoan = models.PositiveIntegerField(null=True)
  locations = models.CharField(max_length=100, choices=LOCATION_CHOICES)

  #LOCATIONS = import from Nigel's
  #LOCATIONS = (('AMK','Ang Mo Kio'), ('SRG', 'Serangoon'), ('WLDS', 'Woodlands'))
  #locations = MultiSelectField(choices=LOCATIONS, max_length=20, default='AMK')
  #REFER TO https://pypi.org/project/django-multiselectfield/0.0.3/

  def __str__(self):
    return self.name

# Create your models here.
