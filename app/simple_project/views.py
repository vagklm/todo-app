from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render

def simple_project(request):
    template = loader.get_template("hello_world.html")
    return HttpResponse(template.render())