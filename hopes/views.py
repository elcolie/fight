from django.core.urlresolvers import reverse_lazy
from django.views.generic import View

from hopes.forms import StudentForm, SchoolForm, OneTimeForm, SpecificDateTimeForm
from hopes.models import Student, School, OneTime, SpecificDateTime
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

"""-----------------------------------------------------------"""
from django.shortcuts import render_to_response, render
from django.template import RequestContext, loader


class ListSpecDateTime(View):

    def index(self, request):
        template = loader.get_template('hopes/simple_spec.html')
        context = {
            'spec_list' : 'Test my string',
        }
        return render(request, 'hopes/simple_spec.html', context)


class CreateSpecDateTime(CreateView):
    model = SpecificDateTime
    form_class = SpecificDateTimeForm
    success_url = reverse_lazy('list_spec_time')


class EditSpecDateTime(UpdateView):
    model = SpecificDateTime
    form_class = SpecificDateTimeForm
    success_url = reverse_lazy('list_spec_time')


class DeleteSpecDateTime(DeleteView):
    model = SpecificDateTime
    success_url = reverse_lazy('list_spec_time')