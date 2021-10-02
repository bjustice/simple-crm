from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class AddRecordGroupForm(forms.Form):
    group_name = forms.CharField(label='Group Name', max_length=100)
    company = forms.CharField(label='Company', max_length=100)
    numberOfFields = forms.IntegerField(label='Number of Fields')
