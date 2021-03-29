from django.db import models
from django.contrib.gis.db import models as gis_models
from django.contrib.gis.db.models import Manager as GeoManager
# Create your models here.


class Incidence(models.Model):
    name = models.CharField(max_length=255)
    location = gis_models.PointField(srid=4326)
    objects = GeoManager()
    
    def __str__(self):
        return self.name