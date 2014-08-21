from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from ProductManagement import models

import datetime


# Create your views here.
from django.shortcuts import render_to_response


def products_list(request):

    products_list_return = models.Product.objects.all()
    return render(request, "products\product_list.html", {"item_list": models.Product.objects.all()})

    #return render_to_response('base.html', )


def product(request, product_id):
    return HttpResponse("You're looking at product %s." % product_id)

def index(request):
    return HttpResponse("Hello, world. You're at the poll index.")