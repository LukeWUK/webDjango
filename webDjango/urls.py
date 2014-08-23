from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.conf import settings

from clock.views import current_datetime


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'webDjango.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^products/', include('ProductManagement.urls')),
    url(r'^sales/', include('Sales.urls')),
    url(r'^contacts/', include('Contacts.urls')),


    (r'^time/$', current_datetime),
    url(r'^admin/', include(admin.site.urls)),

)












if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )
urlpatterns += staticfiles_urlpatterns()