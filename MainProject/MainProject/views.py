from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello, Swarup. You are at your Profile home page")
    return render(request, 'index.html')

def about(request):
    return HttpResponse("Hello, Swarup. You are at your Profile about page")

def contact(request):
    return HttpResponse("Hello, Swarup. You are at your Profile contact page")