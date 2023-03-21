from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Neighbourhood
import requests
from collections import Counter


# Create your views here.

def home(response):
    return render(response, "main/home.html", {})

def neighbourhood_chart(response):

    neighbourhoods = requests.get('https://data.eindhoven.nl/api/records/1.0/search/?dataset=buurten&q=&fields=buurtcode,buurtnaam&rows=10000')
    neighbourhoods_data = neighbourhoods.json()

    neighbourhood_records = neighbourhoods_data['records']
    main_data_array = []
    for record in neighbourhood_records:
        main_data_array.append({"name": record['fields'].get('buurtnaam'), "code": record['fields'].get('buurtcode'), "waste_bins": 0, "residents": 0})


    # Add waste bins to the array
    waste_bins = requests.get('https://data.eindhoven.nl/api/records/1.0/search/?dataset=afvalbakken0&q=&rows=10000&fields=buurt')
    waste_bins_data = waste_bins.json()

    counter = Counter(neighbourhood['fields'].get('buurt') for neighbourhood in waste_bins_data['records'])

    waste_bins_array = []
    for name, waste_bins in counter.items():
        waste_bins_array.append({"name": name, "waste_bins": waste_bins})

    # First, create a dictionary from the second list for quick lookup
    waste_bins_dict = {item['name']: item for item in waste_bins_array}

    # Then, iterate over the first list and add the corresponding object from the second list
    for item in main_data_array:
        if item['name'] in waste_bins_dict:
            second_item = waste_bins_dict[item['name']]
            item['waste_bins'] = second_item['waste_bins']

    # Add residents to the array
    residents = requests.get('https://data.eindhoven.nl/api/records/1.0/search/?dataset=selectiontableasjsonashx&q=&rows=10000&refine.jaar=2023&fields=buurtcode,totaal_aantal_inwoners')
    residents_data = residents.json()

    residents_array = []
    for neighbourhood in residents_data['records']:
        residents_array.append({"code": neighbourhood['fields'].get('buurtcode'), "residents": neighbourhood['fields'].get('totaal_aantal_inwoners')})

    # First, create a dictionary from the second list for quick lookup
    residents_dict = {item['code']: item for item in residents_array}

    # Then, iterate over the first list and add the corresponding object from the second list
    for item in main_data_array:
        if item['code'] in residents_dict:
            second_item = residents_dict[item['code']]
            if second_item['residents'] is None:
                item['residents'] = 0
            else:
                item['residents'] = second_item['residents']

    chart_data = []
    for item in main_data_array:
        if item.get('residents') == 0:
            item['residents'] = 1
        if item.get('waste_bins') == 0:
            item['waste_bins'] = 1

        if item.get('residents')/item.get('waste_bins') < 39 and item.get('waste_bins') > 50 or item.get('residents')/item.get('waste_bins') > 130 and item.get('residents') > 1500:
            chart_data.append({'label': item.get('name') + " (Residents, Waste bins)", 'data': [{ 'x': item.get('residents'), 'y': item.get('waste_bins') }], 'borderColor': '#ff3d3d', 'backgroundColor': '#ff3d3d'})
        else:
            chart_data.append({'label': item.get('name') + " (Residents, Waste bins)", 'data': [{ 'x': item.get('residents'), 'y': item.get('waste_bins') }], 'borderColor': '#c9c9c9', 'backgroundColor': '#c9c9c9'})

    return JsonResponse(data=chart_data, safe=False)

def neighbourhoods(response):
    neighbourhoods = requests.get('https://data.eindhoven.nl/api/records/1.0/search/?dataset=buurten&q=&fields=buurtcode,buurtnaam&rows=10000')
    neighbourhoods_data = neighbourhoods.json()

    neighbourhood_records = neighbourhoods_data['records']
    main_data_array = []
    for record in neighbourhood_records:
        main_data_array.append({"name": record['fields'].get('buurtnaam'), "code": record['fields'].get('buurtcode'), "waste_bins": 0, "residents": 0})


    # Add waste bins to the array
    waste_bins = requests.get('https://data.eindhoven.nl/api/records/1.0/search/?dataset=afvalbakken0&q=&rows=10000&fields=buurt')
    waste_bins_data = waste_bins.json()

    counter = Counter(neighbourhood['fields'].get('buurt') for neighbourhood in waste_bins_data['records'])

    waste_bins_array = []
    for name, waste_bins in counter.items():
        waste_bins_array.append({"name": name, "waste_bins": waste_bins})

    # First, create a dictionary from the second list for quick lookup
    waste_bins_dict = {item['name']: item for item in waste_bins_array}

    # Then, iterate over the first list and add the corresponding object from the second list
    for item in main_data_array:
        if item['name'] in waste_bins_dict:
            second_item = waste_bins_dict[item['name']]
            item['waste_bins'] = second_item['waste_bins']

    # Add residents to the array
    residents = requests.get('https://data.eindhoven.nl/api/records/1.0/search/?dataset=selectiontableasjsonashx&q=&rows=10000&refine.jaar=2023&fields=buurtcode,totaal_aantal_inwoners')
    residents_data = residents.json()

    residents_array = []
    for neighbourhood in residents_data['records']:
        residents_array.append({"code": neighbourhood['fields'].get('buurtcode'), "residents": neighbourhood['fields'].get('totaal_aantal_inwoners')})

    # First, create a dictionary from the second list for quick lookup
    residents_dict = {item['code']: item for item in residents_array}

    # Then, iterate over the first list and add the corresponding object from the second list
    for item in main_data_array:
        if item['code'] in residents_dict:
            second_item = residents_dict[item['code']]
            if second_item['residents'] is None:
                item['residents'] = 0
            else:
                item['residents'] = second_item['residents']

    return render(response, "main/neighbourhoods.html", {"data": main_data_array, "length": len(main_data_array)})

def neighbourhood(response, id):
    x = Neighbourhood.objects.get(id=id)
    return render(response, "main/neighbourhood.html", {"neighbourhood": x})

