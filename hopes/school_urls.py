from django.conf.urls import patterns, include, url
from hopes.models import School
from hopes.views import ListSchools, CreateSchool, EditSchool, DeleteSchool

urlpatterns = [
    url(r'^$', ListSchools.as_view(), name='list_schools'),
    url(r'^create/$', CreateSchool.as_view(), name='create_school'),
    url(r'^edit/(?P<pk>\d+)/$', EditSchool.as_view(), name='edit_school'),
    url(r'^delete/(?P<pk>\d+)/$', DeleteSchool.as_view(), name='delete_school'),
]

