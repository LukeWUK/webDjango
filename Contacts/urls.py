from django.conf.urls import patterns, url

from Contacts import views


urlpatterns = patterns('',
                       url(r'^$',  views.contacts_list, name='contacts$')
                       )

