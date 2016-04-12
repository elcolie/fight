from django.conf.urls import patterns, include, url
from hopes.models import OneTime
from hopes.views import ListOneTime, CreateOneTime, EditOneTime, DeleteOneTime

urlpatterns = [
    url(r'^$', ListOneTime.as_view(), name='list_onetime'),
    url(r'^create/$', CreateOneTime.as_view(), name='create_onetime'),
    url(r'^edit/(?P<pk>\d+)/$', EditOneTime.as_view(), name='edit_onetime'),
    url(r'^delete/(?P<pk>\d+)/$', DeleteOneTime.as_view(), name='delete_onetime'),
]

