from django.shortcuts import render
from django.http import HttpResponse

from .models import GeneralStat



def index(request):
    template = 'pages/dashboard.html'
    general_list = GeneralStat.objects.all()
    stars = {
        'volod9_podkidnoi': 0,
        'pasha_potnii': 0,
        'vlados_cabardos': 0,
        'egor_hardcore': 0,
        'miron_priton': 0,
    }
    for item in general_list:
        maxvalue = {
            'volod9_podkidnoi': float(item.volod9_podkidnoi),
            'pasha_potnii': float(item.pasha_potnii),
            'vlados_cabardos': float(item.vlados_cabardos),
            'egor_hardcore': float(item.egor_hardcore),
            'miron_priton': float(item.miron_priton),
        }
        max_variable = max(maxvalue, key=maxvalue.get)
        stars[max_variable] += 1
    wins = GeneralStat.objects.get(pk=79)
    defeats = GeneralStat.objects.get(pk=40)
    context = {'general_list': general_list,
               'wins': wins,
               'defeats': defeats,
               'stars': stars,
               }
    return render(request, template, context)

