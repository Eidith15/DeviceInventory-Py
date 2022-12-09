from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ListPC
from django.template import loader
from django.urls import reverse


def index(request):
    context = {'segment': 'listpc'}
    template = loader.get_template('listpc/indexpc.html')
    return HttpResponse(template.render(context, request))

def add(request): 
    template = loader.get_template('listpc/add.html')
    return HttpResponse(template.render({},request))    

def addrecord(request):
    x = request.POST['first']
    y = request.POST['last']
    name = ListPC(firstname=x,lastname=y)
    name.save()
    return HttpResponseRedirect(reverse('indexpc.html'))

def delete(request, id):
    name = ListPC.objects.get(id=id)
    name.delete()
    return HttpResponseRedirect(reverse('listpc/indexpc.html'))

def update(request, id):
    name = ListPC.objects.get(id=id)
    template = loader.get_template('listpc/update.html')
    context = {
        'name' : name
    }
    return HttpResponse(template.render(context, request))

def updaterecord(request, id):
    first = request.POST['first']
    last = request.POST['last']
    name = ListPC.objects.get(id=id)
    name.firstname = first
    name.lastname = last
    name.save()
    return HttpResponseRedirect(reverse('listpc/indexpc.html'))