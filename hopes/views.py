from django.core.urlresolvers import reverse_lazy

from hopes.forms import StudentForm, SchoolForm, OneTimeForm
from hopes.models import Student, School, OneTime
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


"""----------------------------------------------------------"""


class ListOneTime(ListView):
    model = OneTime


class CreateOneTime(CreateView):
    model = OneTime
    form_class = OneTimeForm
    success_url = reverse_lazy('list_onetime')


class EditOneTime(UpdateView):
    model = OneTime
    form_class = OneTimeForm
    success_url = reverse_lazy('list_onetime')


class DeleteOneTime(DeleteView):
    model = OneTime
    success_url = reverse_lazy('list_onetime')

