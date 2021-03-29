from django.contrib import admin
from .models import Incidence
from leaflet.admin import LeafletGeoAdmin
# Register your models here.


class IncidenceAdmin(LeafletGeoAdmin, admin.ModelAdmin):
    list_display = ['name','location']
admin.site.register(Incidence, IncidenceAdmin)
