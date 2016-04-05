from django.forms import ModelForm
from .models import Student, School


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'surname', 'country', 'birthDate', 'weight_kg', 'blood',
                  'height_cm', 'primary_school', 'secondary_school']


class SchoolForm(ModelForm):
    class Meta:
        model = School
        fields = ['name', 'address', 'region', 'postcode', 'country', 'build_date']


