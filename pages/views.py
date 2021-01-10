from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def homeView(request):
    return HttpResponse("<h1><i>Hello, World!</i></h1>")
