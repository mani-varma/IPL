from iplapp.models import *
from django import forms

class LoginForm(forms.Form):
    username=forms.CharField(
            required=True,
            widget=forms.TextInput(attrs={'class':'input','placeholder':'User Name'})
    )
    password=forms.CharField(
            required=True,
            widget = forms.PasswordInput(attrs={'class': 'input', 'placeholder': 'Password'})
    )

class SignupForm(forms.Form):
    first_name = forms.CharField(
        max_length=75,
        required = True,
        widget = forms.TextInput(attrs={'class': 'input', 'placeholder': 'First Name'})
    )
    last_name = forms.CharField(
        max_length = 75,
        required = True,
        widget = forms.TextInput(attrs={'class': 'input', 'placeholder': 'Last Name'})
    )
    email=forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'class':'input','placeholder':'Email'})
    )
    username = forms.CharField(
        max_length = 75,
        required = True,
        widget = forms.TextInput(attrs={'class': 'input', 'placeholder': 'User Name'})
    )
    password = forms.CharField(
        max_length = 75,
        required = True,
        widget = forms.PasswordInput(attrs={'class': 'input', 'placeholder': 'Password'})
    )