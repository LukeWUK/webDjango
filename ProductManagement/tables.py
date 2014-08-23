import django_tables2 as tables
from ProductManagement import models

class ProductTable(tables.Table):


    class Meta:
        model = models.Product
        attrs = {"class": "paleblue"}