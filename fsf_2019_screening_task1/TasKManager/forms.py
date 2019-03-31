from django import forms
from .models import SignUp, Team


class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), required=True)
    confrom_pass = forms.CharField(widget=forms.PasswordInput(), required=True)

    class Meta:
        model = SignUp
        fields = '__all__'


class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), required=True)

    class Meta:
        model = SignUp
        fields = ['email_id', 'password']


class CreateTeam(forms.ModelForm):
    class Meta:
        creator_name = forms.CharField
        model = Team
        fields = '__all__'
