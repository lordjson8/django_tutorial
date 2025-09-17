
from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username','password']


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirmation_password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username','password']

  
    