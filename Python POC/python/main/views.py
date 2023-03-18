from django.shortcuts import render
from django.http import HttpResponse
from .models import Neighbourhood

# Create your views here.

def index(response, id):
    x = Neighbourhood.objects.get(id=id)
    return HttpResponse("<h1>%s<h1>" % x.name)
