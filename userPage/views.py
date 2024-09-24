from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def my_userPage(request):
    return HttpResponse("my user page")
