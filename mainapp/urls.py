from django.urls import path
from .views import IndexView, CountyDataView, IncidenceView, GetNearestDrip

app_name = 'mainapp'

urlpatterns = [
    path('', IndexView, name='index'),
    path('counties/', CountyDataView, name='counties'),
    path('incidence/', IncidenceView, name='incidences'),
    path('getshops/', GetNearestDrip, name='getshops'),
]
