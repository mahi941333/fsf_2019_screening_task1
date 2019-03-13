from django import forms
from .models import Users


class SignUpForm(forms.ModelForm):
    Password = forms.CharField(widget=forms.PasswordInput(), required=True)
    ConfirmPassword= forms.CharField(widget=forms.PasswordInput(), required=True)

    class Meta:
        model = Users
        fields = ['Name','Username','Email','Password','ConfirmPassword']


class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), required=True)

    class Meta:
        model = Users
        fields = ['Email','Password']
