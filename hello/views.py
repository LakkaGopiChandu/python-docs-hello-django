from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse("Hi to all hope all are doing good,  happy weekend to all and be healthy and wealthy")
