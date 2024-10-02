from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def products(request):
    template=loader.get_template('my_first.html')
    return HttpResponse(template.render())

def second(request):
    template=loader.get_template('second.html')
    return HttpResponse(template.render())
