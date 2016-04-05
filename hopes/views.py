from django.core.urlresolvers import reverse_lazy
from hopes.models import Student, School
from hopes.forms import StudentForm, SchoolForm
from vanilla import CreateView, DeleteView, ListView, UpdateView


class ListStudents(ListView):
    model = Student


class CreateStudent(CreateView):
    model = Student
    form_class = StudentForm
    success_url = reverse_lazy('list_students')


class EditStudent(UpdateView):
    model = Student
    form_class = StudentForm
    success_url = reverse_lazy('list_students')


class DeleteStudent(DeleteView):
    model = Student
    success_url = reverse_lazy('list_students')


"""-----------------------------------------------------------"""


class ListSchools(ListView):
    model = School


class CreateSchool(CreateView):
    model = School
    form_class = SchoolForm
    success_url = reverse_lazy('list_schools')


class EditSchool(UpdateView):
    model = School
    form_class = SchoolForm
    success_url = reverse_lazy('list_schools')


class DeleteSchool(DeleteView):
    model = School
    success_url = reverse_lazy('list_schools')

