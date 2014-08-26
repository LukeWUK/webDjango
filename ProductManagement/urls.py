from django.conf.urls import patterns, url

from ProductManagement import views


urlpatterns = patterns('',
                       #url(r'^$',  views.products_list, name='catalog'),
                       url(r'^$',  views.search, name='search'),
                       url(r'^(?P<product_id>\d+)/$', views.product, name='product'),
                       url(r'^search$',  views.search, name='search')
                       )

