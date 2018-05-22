from django.shortcuts import render

# Create your views here.

def index(request):
	context = {}
	return render(request, "home.html",context)


def contactus(request):
	context = {}
	return render(request, "contactus.html",context)

def menus(request):
	context = {}
	return render(request, "menu.html",context)
