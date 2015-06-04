from django.conf.urls import include, url
from django.contrib import admin
from General.views import index, login, fuckingCSRF

urlpatterns = [
    # Examples:
    # url(r'^$', 'MythicApps.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', index),
    url(r'^login/', login),
    url(r'csrftoken/$', fuckingCSRF),
]

