from django.shortcuts import render
from django.http import HttpResponse
from .models import Neighbourhood

# Create your views here.

def home(response):
    return render(response, "main/home.html", {})

def neighbourhoods(response):
    x = Neighbourhood.objects.all()
    return render(response, "main/neighbourhoods.html", {"neighbourhoods": x})

def neighbourhood(response, id):
    x = Neighbourhood.objects.get(id=id)
    return render(response, "main/neighbourhood.html", {"neighbourhood": x})

