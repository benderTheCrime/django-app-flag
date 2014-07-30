from django.conf.urls import patterns, include, url
from genericinstallation.views import test_page

urlpatterns = patterns('',
    url(r'^test_page', test_page),
)
