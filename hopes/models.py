from django.db import models
from django.utils.translation import ugettext as _

import datetime


class HumanProfile(models.Model):
    """
    Abstract base classes for Humanity
    """

    BLOOD_TYPES = (
        ('A', 'A-type'),
        ('B', 'B-type'),
        ('AB', 'AB-type'),
        ('O', 'O-type'),
    )
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=512)
    country = models.CharField(max_length=46)
    birthDate = models.DateField(_("Date"), default=datetime.date.today)
    weight_kg = models.PositiveSmallIntegerField(default=1)
    blood = models.CharField(max_length=2, choices=BLOOD_TYPES)
    height_cm = models.SmallIntegerField(default=1)

    class Meta:
        abstract = True


class Building(models.Model):
    """
    Abstract base classes for Building
    """
    address = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    postcode = models.CharField(max_length=20)
    country = models.CharField(max_length=46)
    build_date = models.DateField(_("Date"), default=datetime.date.today)

    class Meta:
        abstract = True


class AbstractDateTime(models.Model):
    """
    Abstract base classes for date/time
    """
    start_date = models.DateField(blank=True)
    start_time = models.TimeField(blank=True)
    end_date = models.DateField(blank=True)
    end_time = models.TimeField(blank=True)

    class Meta:
        abstract = True


class ScheduleCode(models.Model):

    TIME_TYPES = (
        ('OneTime', 'One-Time schedule'),
        ('Recurrence', 'Recurrence schedule'),
        ('Specific', 'Specific Date/Time'),
    )
    time_code = models.CharField(max_length=15, choices=TIME_TYPES)

    class Meta:
        abstract = True


class School(Building):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name    # Put name on Django drop down list. Otherwise it filled by objects


class Student(HumanProfile):
    primary_school = models.ForeignKey(School, related_name="prim_school", null=True, blank=True)
    secondary_school = models.ForeignKey(School, related_name="second_school", null=True, blank=True)


class Subject(AbstractDateTime, ScheduleCode):
    """
    Subject contain ID, name, code, start-time, end-time, recurrence-time
    """
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=30)
    schedule_code = models.ForeignKey()     # Let it use foreign key from another table




