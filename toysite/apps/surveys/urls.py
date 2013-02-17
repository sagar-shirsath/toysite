from django.conf.urls.defaults import *


from surveys import views
urlpatterns = patterns('',
    url(r'^list/$',
        views.list,
        name='survey_list'),
    url(r'^add/$',
        views.add,
        name='survey_add'),
    url(r'^summary/$',
        views.summery,
        name='survey_summery'),

)
