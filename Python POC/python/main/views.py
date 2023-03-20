from django.shortcuts import render
from django.http import HttpResponse
from .models import Neighbourhood
import requests
from collections import Counter


# Create your views here.

def home(response):
    return render(response, "main/home.html", {})

def neighbourhoods(response):
    request = requests.get('https://data.eindhoven.nl/api/records/1.0/search/?dataset=afvalbakken0&q=&rows=10000&facet=buurt')
    data = request.json()

    facets = data['facet_groups'][0]['facets']
    facet_values = []
    for facet in facets:
        facet_values.append({
            "name": facet['name'],
            "count": facet['count'],
        })

    return render(response, "main/neighbourhoods.html", {"data": facet_values, "length": len(facet_values)})

def neighbourhood(response, id):
    x = Neighbourhood.objects.get(id=id)
    return render(response, "main/neighbourhood.html", {"neighbourhood": x})

