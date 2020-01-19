from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
	return HttpResponse("Rango says hey there partner!" + "<a href='/rango/about/'>About</a>")

def about(request):
	return HttpResponse("Here be the about page brother!" + "<a href='/rango/'>Index</a>")