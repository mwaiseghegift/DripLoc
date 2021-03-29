import os
from django.contrib.gis.utils import LayerMapping
from .models import Counties

from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent

counties_mapping = {
    'objectid': 'OBJECTID',
    'area': 'AREA',
    'perimeter': 'PERIMETER',
    'county3_field': 'COUNTY3_',
    'county3_id': 'COUNTY3_ID',
    'county': 'COUNTY',
    'shape_leng': 'Shape_Leng',
    'shape_area': 'Shape_Area',
    'geom': 'MULTIPOLYGON',
}

counties_shp = os.path.join(BASE_DIR, 'mainapp/data/County.shp')


def run(verbose=True):
    lm = LayerMapping(Counties, counties_shp, counties_mapping, transform=False, encoding='iso-8859-1')
    lm.save(strict=True, verbose=verbose)