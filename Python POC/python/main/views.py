from django.shortcuts import render
from django.http import HttpResponse
from .models import Neighbourhood
import requests

# Create your views here.

def home(response):
    return render(response, "main/home.html", {})

def neighbourhoods(response):
    nbhs = requests.get('https://data.eindhoven.nl/api/records/1.0/search/?dataset=afvalbakken0&q=&rows=10000&sort=buurt&facet=stadsdeel&facet=buurt&facet=straat&facet=eigenaar&facet=beheerder&facet=soort&facet=voet&facet=kleur&facet=locatie&facet=inhoud')
    data = nbhs.json()
    return render(response, "main/neighbourhoods.html", {"data": data})

def neighbourhood(response, id):
    x = Neighbourhood.objects.get(id=id)
    return render(response, "main/neighbourhood.html", {"neighbourhood": x})

