from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class AddRecordGroupForm(forms.Form):
    group_name = forms.CharField(label='Group Name', max_length=100)
    company = forms.CharField(label='Company', max_length=100)
    numberOfFields = forms.IntegerField(label='Number of Fields')
    custom_field_count = forms.CharField(widget=forms.HiddenInput())

    def __init__(self, *args, **kwargs):
        custom_fields = kwargs.pop('custom_fields', 0)

        super(AddRecordGroupForm, self).__init__(*args, **kwargs)
        self.fields['custom_field_count'].initial = custom_fields

        for index in range(int(custom_fields)):
            self.fields['custom_field_{index}'.format(index=index)] = \
                forms.CharField()