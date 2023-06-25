from django.shortcuts import render
from django.http import HttpResponse

def simple_project(request):
    return HttpResponse("Hello world!")