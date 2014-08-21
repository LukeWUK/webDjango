from django.conf.urls import patterns, url

from ProductManagement import views


urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^(?P<product_id>.+)/$', views.product, name='product'),
                       url(r'^catalog$', views.products_list, name='catalog$')
                       )

