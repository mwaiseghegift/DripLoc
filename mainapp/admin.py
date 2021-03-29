from django.contrib import admin
from .models import Incidence, Counties
from leaflet.admin import LeafletGeoAdmin
# Register your models here.


class IncidenceAdmin(LeafletGeoAdmin, admin.ModelAdmin):
    list_display = ['name','location']
admin.site.register(Incidence, IncidenceAdmin)


class CountiesAdmin(LeafletGeoAdmin, admin.ModelAdmin):
    list_display = ['county','area']
admin.site.register(Counties, CountiesAdmin)
