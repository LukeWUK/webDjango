from django.shortcuts import render
from django_tables2 import RequestConfig
from Contacts import tables

# Create your views here.

def contacts_list(request):

    data = [{"name": "Bradley"},
            {"name": "Stevie"},
            ]

    contacts_list_return = tables.ContactsTable(data)
    contacts_list_return.paginate(page=request.GET.get('page', 1), per_page=1)
    return render(request, "contacts\contact_list.html", {"item_list": contacts_list_return})

