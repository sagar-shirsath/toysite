from django.conf.urls.defaults import *


from users import views
urlpatterns = patterns('',
    url(r'^login/$',
        views.login,
        name='users_login'),
    url(r'^register/$',
        views.register,
        name='users_register'),

)
