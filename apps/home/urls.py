# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path, include
from apps.home import views as view_home


urlpatterns = [

    # The home page
    path('', view_home.index, name='home'),
    
    # re_path('listpc/', include('apps.listpc.urls'), name='listpc' ),
    # re_path('listap/', include('apps.listap.urls'), name='listap' ),
    # re_path('listcctv/', include('apps.listcctv.urls'), name='listcctv' ),
    # re_path('listemail/', include('apps.listemail.urls'), name='listemail' ),
    # re_path('listprinter/', include('apps.listprinter.urls'), name='listprinter' ),
    # re_path('listscanner/', include('apps.listscanner.urls'), name='listscanner' ),
    # re_path('listserver/', include('apps.listserver.urls'), name='listserver' ),
    
    # Matches any html file
    #re_path(r'^.*\.*', view_home.pages, name='pages'),

    


]
