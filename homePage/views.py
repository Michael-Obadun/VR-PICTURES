from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def my_homePage(request):
    return HttpResponse("my home page")