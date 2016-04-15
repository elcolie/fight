from django.forms import ModelForm
from .models import Student, School, OneTime, SpecificDateTime
from django import forms
from django.utils.translation import ugettext as _
from django.contrib.postgres import forms as pgsql_forms

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'surname', 'country', 'birthDate', 'weight_kg', 'blood',
                  'height_cm', 'primary_school', 'secondary_school']


class SchoolForm(ModelForm):
    class Meta:
        model = School
        fields = ['name', 'address', 'region', 'postcode', 'country', 'build_date']


class OneTimeForm(ModelForm):
    class Meta:
        model = OneTime
        fields = ['start_datetime', 'stop_datetime', 'stop_type', 'lifetime_quantity', 'lifetime_unit']


class SpecificDateTimeForm(ModelForm):

    PERIOD_MIN = 0
    PERIOD_HOUR = 1
    PERIOD_DAY = 2
    PERIOD_MONTH = 3
    PERIOD_YEAR = 4
    PERIOD_FOREVER = 5

    LIFETIME_UNIT = (
        (PERIOD_MIN, _('minutes')),
        (PERIOD_HOUR, _('hours')),
        (PERIOD_DAY, _('days')),
        (PERIOD_MONTH, _('months')),
        (PERIOD_YEAR, _('Stop every year')),
        (PERIOD_FOREVER, _('NonStop')),
    )

    class Meta:
        model = SpecificDateTime
        fields = ['start_datetime', 'stop_datetime',
                  'lifetime_quantity', 'lifetime_unit', 'month_json', 'days_json']

    name = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                     choices=LIFETIME_UNIT)

    json = pgsql_forms.JSONField
