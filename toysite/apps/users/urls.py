from django.conf.urls.defaults import *


from users import views
urlpatterns = patterns('',
    url(r'^logout_me/$',
        views.logout_me,
        name='users_logout_me'),
    url(r'^register/$',
        views.register,
        name='users_register'),
    (r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'users/login.html'}),


)
