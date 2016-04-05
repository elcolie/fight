from django.forms import ModelForm
from .models import Student, School


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'surname', 'country', 'BirthDate', 'Weight(kg)', 'BloodType',
                  'Height(cm)', 'PrimarySchool', 'SecondarySchool']


class SchoolForm(ModelForm):
    class Meta:
        model = School
        fields = ['Name', 'Address', 'Region', 'PostCode', 'Country', 'BuildDate']


