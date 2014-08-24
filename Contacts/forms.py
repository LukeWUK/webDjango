from django import forms

from Contacts import models


class ContactForm(forms.ModelForm):
    class Meta:
        model = models.Contact




