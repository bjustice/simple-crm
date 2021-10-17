from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class AddRecordForm(forms.Form):
    record_type = forms.CharField(label='Record Type', max_length=100)

    def __init__(self, *args, **kwargs):
        custom_fields = kwargs.pop('custom_fields', -1)
        print(custom_fields)

        super(AddRecordForm, self).__init__(*args, **kwargs)
        for index in range(int(custom_fields)):
            self.fields['custom_field_{index}'.format(index=index)] = \
                forms.CharField()


class UpdateRecordForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=100)
    last_name = forms.CharField(label='Last Name', max_length=100)
    record_type = forms.CharField(label='Record Type', max_length=100)

class SelectRecordTypeForm(forms.Form):
    record_type = forms.CharField(label='Record Type', max_length=100)

class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Username",                
                "class": "form-control"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Password",                
                "class": "form-control"
            }
        ))

class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Username",                
                "class": "form-control"
            }
        ))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder" : "Email",                
                "class": "form-control"
            }
        ))
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Password",                
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Password check",                
                "class": "form-control"
            }
        ))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
