from django.conf.urls import patterns, include, url
from hopes.models import Student
from hopes.views import ListStudents, CreateStudent, EditStudent, DeleteStudent

urlpatterns = [
    url(r'^$', ListStudents.as_view(), name='list_students'),
    url(r'^create/$', CreateStudent.as_view(), name='create_student'),
    url(r'^edit/(?P<pk>\d+)/$', EditStudent.as_view(), name='edit_student'),
    url(r'^delete/(?P<pk>\d+)/$', DeleteStudent.as_view(), name='delete_student'),
]

