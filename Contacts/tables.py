import django_tables2 as tables
from Contacts import models


class ContactsTable(tables.Table):
    name = tables.Column()

    class Meta:

        attrs = {"class": "paleblue"}