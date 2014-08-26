from django.db import models

from autoslug import AutoSlugField


# Create your models here.

class Contact(models.Model):
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
    slug = AutoSlugField(populate_from='last_name', unique_with='id')
    photo = models.ImageField(upload_to='product_photo',
                              blank=True)
    email = models.EmailField(blank=True)
    telephone = models.CharField(max_length=15,blank=True)
    house_number = models.CharField(max_length=300, blank=True)
    street = models.CharField(max_length=300, blank=True)
    locality = models.CharField(max_length=300, blank=True)
    town = models.CharField(max_length=300, blank=True)
    postcode = models.CharField(max_length=300, blank=True)
    county = models.CharField(max_length=300, blank=True)
    country = models.CharField(max_length=300, blank=True)

    def __unicode__(self):
        return u'%s: %s' % (self.first_name,
                            self.last_name)