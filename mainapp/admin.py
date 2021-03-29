from django.contrib import admin
from .models import Incidence
# Register your models here.


class IncidenceAdmin(admin.ModelAdmin):
    list_display = ['name','location']
admin.site.register(Incidence, IncidenceAdmin)
