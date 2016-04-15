from django.conf.urls import patterns, include, url
from hopes.models import SpecificDateTime
from hopes.views import ListSpecDateTime, CreateSpecDateTime, EditSpecDateTime, DeleteSpecDateTime

urlpatterns = [
    # url(r'^$', ListSpecDateTime.as_view(), name='list_spec_date_time'),
    url(r'^$', ListSpecDateTime.index, name='list_spec_date_time'),
    url(r'^create/$', CreateSpecDateTime.as_view(), name='create_spec_date_time'),
    url(r'^edit/(?P<pk>\d+)/$', EditSpecDateTime.as_view(), name='edit_spec_date_time'),
    url(r'^delete/(?P<pk>\d+)/$', DeleteSpecDateTime.as_view(), name='delete_spec_date_time'),
]

