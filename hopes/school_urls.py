from django.conf.urls import patterns, include, url
from hopes.models import Student, School
from hopes.views import ListStudents, CreateStudent, EditStudent, DeleteStudent, ListSchools, CreateSchool, EditSchool, DeleteSchool

urlpatterns = [
    url(r'^$', ListStudents.as_view(), name='list_students'),
    url(r'^create/$', CreateStudent.as_view(), name='create_student'),
    url(r'^edit/(?P<pk>\d+)/$', EditStudent.as_view(), name='edit_student'),
    url(r'^delete/(?P<pk>\d+)/$', DeleteStudent.as_view(), name='delete_student'),
    url(r'^$', ListSchools.as_view(), name='list_schools'),
    url(r'^create/$', CreateSchool.as_view(), name='create_school'),
    url(r'^edit/(?P<pk>\d+)/$', EditSchool.as_view(), name='edit_school'),
    url(r'^delete/(?P<pk>\d+)/$', DeleteSchool.as_view(), name='delete_school'),
]

