from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context
from django.http import HttpResponse
from django_tables2 import RequestConfig
from ProductManagement import tables
from ProductManagement import models

import datetime


# Create your views here.
from django.shortcuts import render_to_response


def products_list(request):

    products_list_return = tables.ProductTable(models.Product.objects.all())
    products_list_return.paginate(page=request.GET.get('page', 1), per_page=2)
    return render(request, "products\product_list.html", {"item_list": products_list_return})



def product(request, product_id):
    return HttpResponse("You're looking at product %s." % product_id)

def index(request):
    return HttpResponse("Hello, world. You're at the poll index.")