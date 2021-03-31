from django.shortcuts import render, HttpResponse
from .models import Counties, Incidence
from django.core.serializers import serialize
from django.contrib.gis.geos import fromstr, Point
from django.contrib.gis.db.models.functions import Distance
from django.http import JsonResponse
import json
# Create your views here.

def IndexView(request, *args, **kwargs):
    return render(request, 'index.html')


def CountyDataView(request, *args, **kwargs):
    counties = serialize('geojson', Counties.objects.all())
    return HttpResponse(counties, content_type='json')

def IncidenceView(request, *args, **kwargs):
    incidences = serialize('geojson', Incidence.objects.all())
    return HttpResponse(incidences, content_type='json')


def GetNearestDrip(request, *args, **kwargs):
    if request.method=='POST':
        latitude1 = request.POST.get('latitude')
        longitude1 = request.POST.get('longitude')

        datao = 0.25455511
        print(type(datao))

        floatLatitude = float(latitude1)
        floatLongitude = float(longitude1)
        
        user_location = Point((floatLongitude, floatLatitude), srid=4326)
        queryset = Incidence.objects.annotate(distance=Distance('location', user_location)).order_by('distance')[0:6]

        context = {
            'latitude':floatLatitude,
            'longitude':floatLongitude,
            'queryset':queryset,
        }
        return render(request, 'nearest.html', context)
    return render(request, 'nearest.html')