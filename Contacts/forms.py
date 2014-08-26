from django import forms

from Contacts import models


class Contact_Form(forms.ModelForm):
    class Meta:
        model = models.Contact




