from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


from django.shortcuts import render, get_object_or_404, redirect
from . import forms


def LoginPage(request):
    obj = forms.LoginForm()
    return render(request, 'base.html', {'obj': obj})


def signUpPage(request):
    form = forms.SignUpForm()
    if request.method == 'POST':
        if form.is_valid():
            Name = form.cleaned_data['Name']
            Username = form.cleaned_data['Username']
            Email = form.cleaned_data['Email']
            
            Password = form.cleaned_data['Password']
            ConfirmPassword = form.cleaned_data['ConfirmPassword']
            form.save()
            return redirect("<h2>Hey congo you created your account</h2>")
    else:
        form = forms.SignUpForm()
        return render(request, 'signup.html', {'form': form})

