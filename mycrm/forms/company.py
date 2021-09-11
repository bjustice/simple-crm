from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class AddCompanyForm(forms.Form):
    company_name = forms.CharField(label='Company Name', max_length=100)
