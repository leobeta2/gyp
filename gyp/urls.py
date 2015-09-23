"""gyp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from gyp.views import index, about, location, gallery, gracias
from contactos.views import contactos

urlpatterns = [
    #url(r'^admin/', include(admin.site.urls)),
    
    url(r'^$', index),
    url(r'^inicio/$', index),
    url(r'^sobre/$', about),
    url(r'^productos/', include('productos.urls', namespace="productos")),
    url(r'^ubicacion/$', location),
    url(r'^contacto/$',contactos),
    url(r'^galeria/$',gallery),
    url(r'^contactos/gracias/$',gracias),
]
