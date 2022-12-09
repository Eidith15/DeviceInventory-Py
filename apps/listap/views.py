from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
# Create your views here.

def index(request):
    context = {'segment' : 'listap'}
    template = loader.get_template('listap/indexap.html')
    return HttpResponse(template.render(context, request))

def add(request): 
    template = loader.get_template('listap/add.html')
    return HttpResponse(template.render({},request)) 