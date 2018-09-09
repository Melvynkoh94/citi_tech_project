from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django import forms
from .models import Snippet
from django.core.exceptions import ValidationError
from .choices import *

class UserForm(forms.Form):
  age = forms.IntegerField(initial='30', label='Please define your age, as of this year')
  gender = forms.ChoiceField(choices=GENDER_CHOICES)
  monthlyIncome = forms.IntegerField(initial='3000', label='Please enter your estimated monthly income, rounded to the nearest dollar')
  essentialExpenses = forms.IntegerField(initial='1800', label='Please enter your estimated monthly expenses, rounded to the nearest dollar')
  personalSavings = forms.IntegerField(initial='1200', label='Please enter your personal savings, rounded to the nearest dollar')
  availDownPay = forms.IntegerField(initial='30000', label='Please enter the amount you can afford to downpay, rounded to the nearest dollar')
  existingLoan = forms.IntegerField(initial='1', label='Please enter the number of existing housing loans you have')
  locations = forms.ChoiceField(choices=LOCATION_CHOICES, label='Select Property Location')

  #constructor
  def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
          'age',
          'gender',
          'monthlyIncome',
          'essentialExpenses',
          'personalSavings',
          'availDownPay',
          'existingLoan',
          'locations',
          Submit('submit', 'Submit', css_class='btn-success')
        )


class UserForm_extended(forms.Form):
  y1 = forms.ChoiceField(choices=YES_NO_CHOICES, label='Are you a first time homeowner?')
  y2 = forms.ChoiceField(choices=YES_NO_CHOICES, label='Are you staying within 4km from your parents?')
  y3 = forms.ChoiceField(choices=YES_NO_CHOICES, label='At least 1 of the applicants must have worked continuously for 12 months prior to the flat application, and still be employed at the point of flat application. Is this true for you?')

  #constructor
  def __init__(self, *args, **kwargs):
    super(UserForm_extended, self).__init__(*args, **kwargs)

    self.helper = FormHelper
    self.helper.form_method = 'post'
    self.helper.layout = Layout(
      'y1',
      'y2',
      'y3',
      Submit('submit', 'Submit', css_class='btn_success')
    )


class SnippetForm(forms.ModelForm):

  class Meta:
    model = Snippet
    fields = ('age', 'gender')