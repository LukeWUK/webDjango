from django.conf.urls import patterns, url

from ProductManagement import views


urlpatterns = patterns('',
                       url(r'^$',  views.products_list, name='catalog$'),
                       url(r'^(?P<product_id>.+)/$', views.product, name='product')
                       )

