from django import template
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

def index(request):
    context = {'segment': 'indexhome'}

    html_template = loader.get_template('home/indexhome.html')
    return HttpResponse(html_template.render(context, request))


def pages(request):
    context = {}
    try:

        load_template = request.path.split('/')[-1]
        context['segment'] = load_template

        if load_template == 'admin' : 
            return HttpResponseRedirect(reverse('admin:index'))

        html_template = loader.get_template('home/'+load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))

