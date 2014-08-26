from django.db import models
import datetime
from autoslug import AutoSlugField

# Create your models here.


class Product(models.Model):
    category = models.ForeignKey('CatalogCategory',
                                 related_name='products')
    name = models.CharField(max_length=300)
    slug = AutoSlugField(populate_from='name', unique_with='id')
    description = models.TextField(blank=True)
    photo = models.ImageField(upload_to='product_photo',
                              blank=True)
    manufacturer = models.CharField(max_length=300,
                                    blank=True)
    price = models.DecimalField(max_digits=6,
                                decimal_places=2)
    #attributes = models.ManyToManyField('Attribute')

    def __unicode__(self):
        return u'%s: %s' % (self.manufacturer,
                            self.name)


class CatalogCategory(models.Model):
    parent = models.ForeignKey('self', blank=True, null=True,
                               related_name='children')
    name = models.CharField(max_length=300)
    slug = AutoSlugField(populate_from='name')
    description = models.TextField(blank=True)

    def __unicode__(self):
        if self.parent:
            return u'%s: %s' % (self.parent.name,
                                     self.name)
        return u': %s' % (self.name)


class ProductDetail(models.Model):
    """
     The ``ProductDetail`` model represents information unique to a
     specific product. This is a generic design that can be used
     to extend the information contained in the ``Product`` model with
     specific, extra details.
    """

    product = models.ForeignKey('Product',
                                related_name='details')
    attribute = models.ForeignKey('ProductAttribute')
    value = models.CharField(max_length=500)
    description = models.TextField(blank=True)

    def __unicode__(self):
        return u'%s: %s - %s' % (self.product,
                                 self.attribute,
                                 self.value)


class ProductAttribute(models.Model):
    """
     The "ProductAttribute" model represents a class of feature found
     across a set of products. It does not store any data values
     related to the attribute, but only describes what kind of a
     product feature we are trying to capture. Possible attributes
     include things such as materials, colors, sizes, and many, many
     more.
    """

    name = models.CharField(max_length=300)
    description = models.TextField(blank=True)

    def __unicode__(self):
        return u'%s' % self.name