from django.db import models
from django.utils.translation import ugettext as _

import datetime


class HumanProfile(models.Model):
    """
    Abstract base classes for Humanity
    """
    BLOOD_A = 'A'
    BLOOD_B = 'B'
    BLOOD_AB = 'AB'
    BLOOD_O = 'O'

    BLOOD_TYPES = (
        (BLOOD_A, _('A-type')),
        (BLOOD_B, _('B-type')),
        (BLOOD_AB, _('AB-type')),
        (BLOOD_O, _('O-type')),
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
    PERIOD_MIN = 0
    PERIOD_HOUR = 1
    PERIOD_DAY = 2
    PERIOD_MONTH = 3
    PERIOD_YEAR = 4
    PERIOD_FOREVER = 5

    STOP_PERIODS = (
        (PERIOD_MIN, _('Stop every minutes')),
        (PERIOD_HOUR, _('Stop every hour')),
        (PERIOD_DAY, _('Stop every day')),
        (PERIOD_MONTH, _('Stop every month')),
        (PERIOD_YEAR, _('Stop every year')),
        (PERIOD_FOREVER, _('Not start again'))
    )

    start_date = models.DateField(blank=True, null=True)
    start_time = models.TimeField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)

    period = models.CharField(max_length=10, choices=STOP_PERIODS)

    class Meta:
        abstract = True


class School(Building):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name    # Put name on Django drop down list. Otherwise it filled by objects


class Student(HumanProfile):
    primary_school = models.ForeignKey(School, related_name="prim_school", null=True, blank=True)
    secondary_school = models.ForeignKey(School, related_name="second_school", null=True, blank=True)


class OneTime(AbstractDateTime):
    """Has start_date, start_time, end_date, end_time"""
    STOP_TYPES = (
        ('Date', 'Date/Time type'),
        ('Period', 'Life time min, hr, day, month, forever'),
    )
    type = models.CharField(max_length=10, choices=STOP_TYPES)


class RecurrenceTime(AbstractDateTime):

    RECURRENCE_TYPES = (
        ('Day', 'String representation of day'),
        ('Number', 'Periodically run on day count period'),
        ('Month', 'Monthly period'),
    )

    monday = models.BooleanField(default=False)
    tuesday = models.BooleanField(default=False)
    wednesday = models.BooleanField(default=False)
    thursday = models.BooleanField(default=False)
    friday = models.BooleanField(default=False)
    saturday = models.BooleanField(default=False)
    sunday = models.BooleanField(default=False)

    """
    Date on number?
    Should I use single record handle it
    """

    january = models.BooleanField(default=False)
    february = models.BooleanField(default=False)
    march = models.BooleanField(default=False)
    april = models.BooleanField(default=False)
    may = models.BooleanField(default=False)
    june = models.BooleanField(default=False)
    july = models.BooleanField(default=False)
    august = models.BooleanField(default=False)
    september = models.BooleanField(default=False)
    october = models.BooleanField(default=False)
    november = models.BooleanField(default=False)
    december = models.BooleanField(default=False)


class SpecDateTime(AbstractDateTime):
    class Meta:
        abstract = False
