from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .models import Users

from django.shortcuts import render, get_object_or_404, redirect
from . import forms


def LoginPage(request):
   if request.method == 'POST':
        print("me kaha")
        obj = forms.LoginForm(request.POST)
        if obj.is_valid():
            model = Users
            Email = obj.cleaned_data['Email']
            Password = obj.cleaned_data['Password']
            typed_email = ''
            typed_pass = ''
            try:
                typed_email = model.objects.filter(Email=Email).only("email").values_list()[0][2]
                typed_pass = model.objects.filter(Password=Password).only("email").values_list()[0][4]
                typed_email = str(typed_email)
                typed_pass = str(typed_pass)
                print("----------", typed_email, typed_pass)
            except:
                pass

        if Email == typed_email and Password == typed_pass:
                print("entered in box")
                return render(request, 'afterLogin.html', {'email': Email})
        else:
                return HttpResponse("<h2>User may not exist , please signUp first</h2>")
   else:
        obj = forms.LoginForm()
        print("yaha")
        return render(request, 'base.html', {'obj': obj})


   
def signUpPage(request):
    
    if request.method == 'POST':
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            Name = form.cleaned_data['Name']
            Username = form.cleaned_data['Username']
            Email = form.cleaned_data['Email']
            Password = form.cleaned_data['Password']
            ConfirmPassword = form.cleaned_data['ConfirmPassword']
            form.save(commit=True)
            return HttpResponse("<h2>Hey congo you created your account</h2>")
    else:
        form = forms.SignUpForm()
        return render(request, 'signup.html', {'form': form})



def welcomePage(request):
    return render(request, 'afterLogin.html', None)
