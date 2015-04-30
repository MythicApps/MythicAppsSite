from django.conf.urls import include, url
from django.contrib import admin
from Applications.views import create, sponsorCreate

urlpatterns = [
    # Examples:
    # url(r'^$', 'MythicApps.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^create/', create),
    url(r'^sponsorCreate/', sponsorCreate),
]

