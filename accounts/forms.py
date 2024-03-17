from django import forms

from .models import *


class LoginForm(forms.Form):
    username = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "form-control",
                'style':"color:#ae00e5"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                'style':"color:#ae00e5"
            }
        )
    )