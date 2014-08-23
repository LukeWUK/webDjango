from django.conf.urls import patterns, url

from Sales import views


urlpatterns = patterns('',
                       url(r'^$',  views.make_sales, name='contacts$')
                       )

