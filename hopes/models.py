from django.db import models
from django.utils.translation import ugettext as _
from datetime import datetime
# import datetime
# Use this because migration start_datetime = models.DateTimeField(default=datetime.now, blank=False)
# AttributeError: module 'datetime' has no attribute 'now'


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
    birthDate = models.DateField(_("Date"), default=datetime.today)
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
    build_date = models.DateField(_("Date"), default=datetime.today)

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
        (PERIOD_FOREVER, _('Not start again')),
    )

    start_date = models.DateField(blank=True, null=True)
    start_time = models.TimeField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)

    period = models.IntegerField(choices=STOP_PERIODS, default=0)

    class Meta:
        abstract = True


class AbstractDataTimeType(models.Model):
    """Do not thing just define 3 types of schedule.
    1. One-Time
    2. Recurrence
    3. Specific Date/Time
    """
    SCHEDULE_ONETIME = 0
    SCHEDULE_RECURRENCE = 1
    SCHEDULE_SPECIFIC = 2   # Specific Date/Time
    SCHEDULE_TYPES = (
        (SCHEDULE_ONETIME, _('One-Time type')),
        (SCHEDULE_RECURRENCE, _('Recurrence type')),
        (SCHEDULE_SPECIFIC, _('Specific date time type')),
    )
    schedule_category = models.IntegerField(choices=SCHEDULE_TYPES, default=0)


class School(Building):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name    # Put name on Django drop down list. Otherwise it filled by objects


class Student(HumanProfile):
    primary_school = models.ForeignKey(School, related_name="prim_school", null=True, blank=True)
    secondary_school = models.ForeignKey(School, related_name="second_school", null=True, blank=True)


class OneTime(AbstractDataTimeType):
    """Has start_date, start_time, end_date, end_time"""

    ONETIME_DATETIME = 0
    ONETIME_PERIOD = 1
    STOP_TYPES = (
        (ONETIME_DATETIME, _('Date/Time')),
        (ONETIME_PERIOD, _('Period')),
    )

    PERIOD_MIN = 0
    PERIOD_HOUR = 1
    PERIOD_DAY = 2
    PERIOD_MONTH = 3
    PERIOD_YEAR = 4
    PERIOD_FOREVER = 5

    LIFETIME_UNIT = (
        (PERIOD_MIN, _('Stop every minutes')),
        (PERIOD_HOUR, _('Stop every hour')),
        (PERIOD_DAY, _('Stop every day')),
        (PERIOD_MONTH, _('Stop every month')),
        (PERIOD_YEAR, _('Stop every year')),
        (PERIOD_FOREVER, _('NonStop')),
    )

    stop_type = models.PositiveSmallIntegerField(choices=STOP_TYPES, default=0)
    start_datetime = models.DateTimeField(default=datetime.now, blank=True, null=True)
    stop_datetime = models.DateTimeField(default=datetime.now, blank=True, null=True)
    lifetime_quantity = models.PositiveIntegerField(blank=True, null=True)
    lifetime_unit = models.PositiveSmallIntegerField(choices=LIFETIME_UNIT, default=0, blank=True, null=True)

    def get_stop_datetime(self):
        if self.stop_type == self.ONETIME_PERIOD:
            return ""
        else:
            return self.stop_datetime

    def get_lifetime_quantity(self):
        if self.stop_type == self.ONETIME_PERIOD:
            return self.lifetime_quantity
        else:
            return "x"


