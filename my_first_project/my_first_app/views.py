from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def my_first_app(request):
    return HttpResponse("Hello, Welcome to the members page")
