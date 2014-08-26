from django.shortcuts import render
from django_tables2 import RequestConfig
from Contacts import tables
from Contacts import forms
import models
from django.http import response
from Contacts import forms

# Create your views here.


def contacts_list(request):

    data = [{"name": "Bradley"},
            {"name": "Stevie"},
            ]

    contacts_list_return = tables.ContactsTable(data)
    contacts_list_return.paginate(page=request.GET.get('page', 1), per_page=1)
    return render(request, "contacts\contact_list.html", {"item_list": contacts_list_return})


def contacts_form(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = forms.Contact_Form(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            form.save()
            # redirect to a new URL:
            return response.HttpResponseRedirect('.')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = forms.Contact_Form()

    return render(request, 'contacts\contact_form.html', {'form': form})
