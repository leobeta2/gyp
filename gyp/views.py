from django.http import Http404, HttpResponse
from django.shortcuts import render

def hola(request):#para cada funcion de vista por convencion se toma el request
    return HttpResponse("Hola Mundo")

def index(request):
	return render(request, 'index.html')