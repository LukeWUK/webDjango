from django.db import models

from autoslug import AutoSlugField


# Create your models here.

class Contact(models.Model):
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
    slug = AutoSlugField(populate_from='first_name', unique_with='id')
    photo = models.ImageField(upload_to='product_photo',
                              blank=True)
    email = models.EmailField()
    telephone = models.CharField(max_length=15)
    house_number = models.CharField(max_length=300)
    street = models.CharField(max_length=300)
    locality = models.CharField(max_length=300)
    town = models.CharField(max_length=300)
    postcode = models.CharField(max_length=300)
    county = models.CharField(max_length=300)
    country = models.CharField(max_length=300)

    def __unicode__(self):
        return u'%s: %s' % (self.first_name,
                            self.last_name)