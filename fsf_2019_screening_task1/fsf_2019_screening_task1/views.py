from django.views.generic import (TemplateView, ListView, DeleteView, DetailView, CreateView, UpdateView)
from django.shortcuts import render, get_object_or_404, redirect


def LoginPage(request):
    return render(request, 'base.html', context=None)
