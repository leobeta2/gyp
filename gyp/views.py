from django.http import Http404, HttpResponse
from django.shortcuts import render


def index(request):
	return render(request, 'index.html')

def about(request):
	return render(request, 'about.html')

def location(request):
	return render(request, 'location.html')