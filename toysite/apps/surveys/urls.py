from django.conf.urls.defaults import *


from surveys import views
urlpatterns = patterns('',
    url(r'^list/$',
        views.list,
        name='survey_list'),
    url(r'^add/$',
        views.add,
        name='survey_add'),
    url(r'^summary/(?P<id>\d+)$',
        views.summery,
        name='survey_summery'),

    url(r'^submit/(?P<id>\d+)$',
        views.submit,
        name='survey_submit'),

)
