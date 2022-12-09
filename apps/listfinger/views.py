from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
# Create your views here.

def index(request):
    context = {'segment' : 'listfinger'}
    template = loader.get_template('listfinger/indexfinger.html')
    return HttpResponse(template.render(context, request))