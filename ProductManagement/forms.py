from django import forms
from ProductManagement import models


class ProductForm(forms.ModelForm):
    class Meta:
        model = models.Product
        #fields = ['name', 'manufacturer', 'description']