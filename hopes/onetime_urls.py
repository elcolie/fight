from django.conf.urls import patterns, include, url
from hopes.models import OneTime
from hopes.views import ListOneTime

urlpatterns = [
    url(r'^$', ListOneTime.as_view(), name='list_onetime'),
    url(r'^create/$', CreateStudent.as_view(), name='create_student'),
    # url(r'^edit/(?P<pk>\d+)/$', EditStudent.as_view(), name='edit_student'),
    # url(r'^delete/(?P<pk>\d+)/$', DeleteStudent.as_view(), name='delete_student'),
]

