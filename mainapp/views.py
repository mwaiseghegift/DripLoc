from django.shortcuts import render, HttpResponse
from .models import Counties, Incidence
from django.core.serializers import serialize
# Create your views here.

def IndexView(request, *args, **kwargs):
    return render(request, 'index.html')


def CountyDataView(request, *args, **kwargs):
    counties = serialize('geojson', Counties.objects.all())
    return HttpResponse(counties, content_type='json')

def IncidenceView(request, *args, **kwargs):
    pass
