
from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context
from django.http import response
from django_tables2 import RequestConfig
from ProductManagement import tables
from ProductManagement import models
from django.db.models import Q
from django.shortcuts import render_to_response
from ProductManagement import forms

def search(request):
    query = request.GET.get('q', '')
    if query:
        qset = (
            Q(manufacturer__icontains=query) |
            Q(name__icontains=query)
        )
        results = tables.ProductTable(models.Product.objects.filter(qset).distinct())

        RequestConfig(request).configure(results)
        results.paginate(page=request.GET.get('page', 1), per_page=3)

    else:

        results = tables.ProductTable(models.Product.objects.all())

        RequestConfig(request).configure(results)
        results.paginate(page=request.GET.get('page', 1), per_page=3)

    return render(request,"products/search.html", {
        "results": results,
        "query": query
    })



def products_list(request):

    products_list_return = tables.ProductTable(models.Product.objects.all())
    RequestConfig(request).configure(products_list_return)
    products_list_return.paginate(page=request.GET.get('page', 1), per_page=3)
    return render(request, "products\product_list.html", {"item_list": products_list_return})


def product(request, product_id):
    try:
        data = models.Product.objects.get(id=product_id)
    except models.Product.DoesNotExist:
        return HttpResponse("Product %s does not exist in database." % product_id)

    # if this is a POST request we need to process the form data
    if request.method == 'POST':

        # create a form instance and populate it with data from the request:
        form = forms.ProductForm(request.POST, instance=data)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            form.save()
            # redirect to a new URL:
            return response.HttpResponseRedirect('.')

    # if a GET (or any other method) we'll create a blank form
    else:

        form = forms.ProductForm(instance=data)

        return render(request, 'products\product_detail.html', {'form': form})




