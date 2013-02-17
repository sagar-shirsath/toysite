from django.conf.urls import patterns, include, url

from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()


urlpatterns = patterns('',
    url(r'^$','surveys.views.list',{},name = "surveys_list"),
    url(r'^user/',include('users.urls'),{},name = "user"),
    url(r'^survey/',include('surveys.urls'),{},name = "surveys"),
    url(r'^admin/', include(admin.site.urls)),


    # Examples:
    # url(r'^$', 'toysite.views.home', name='home'),
    # url(r'^toysite/', include('toysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
        #        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    )
