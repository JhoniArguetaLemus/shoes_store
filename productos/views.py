from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Men, Woman


def products(request):
    template=loader.get_template('home.html')
    return HttpResponse(template.render())

def mens(request):
    template=loader.get_template('mens.html')
    mensShoes=Men.objects.all()
    context={'shoes':mensShoes}
    return HttpResponse(template.render(context, request))

def women(request):
    template=loader.get_template('women.html')
    womenShoes=Woman.objects.all()
    context={'shoes':womenShoes}
    return HttpResponse(template.render(context, request))

def buscar_productos(request):

    query=request.GET.get('q')
    results=None
    if query:
        results=Woman.objects.filter(shoe_name__icontains=query)| Woman.objects.filter(shoe_description__icontains=query)
    elif not query:
        results=Woman.objects.all()
        
    
    return render(request,'women.html', {'results':results, 'query':query} )