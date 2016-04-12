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

    class Meta:
        abstract = True


class AbstractLifeTime(models.Model):
    """Life time abstract class
    """
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
    lifetime_id = models.AutoField(primary_key=True)
    lifetime_quantity = models.PositiveIntegerField(blank=True, null=True)
    lifetime_unit = models.PositiveSmallIntegerField(choices=LIFETIME_UNIT, default=0, blank=True, null=True)

    class Meta:
        abstract = True


class AbstractSpecificDateTime(models.Model):
    """Abstract Class SpecificDateTime
    """
    from django.contrib.postgres.fields import JSONField
    spec_date_time = models.AutoField(primary_key=True)
    start_datetime = models.DateTimeField(default=datetime.now, blank=True, null=True)
    stop_datetime = models.DateTimeField(default=datetime.now, blank=True, null=True)
    month_json = JSONField()
    days_json = JSONField()

    # class Meta:
    #     abstract = True



class School(Building):
    # school_id = models.AutoField(primary_key=True) # No need primary key
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name    # Put name on Django drop down list. Otherwise it filled by objects


class Student(HumanProfile):
    # student_id = models.AutoField(primary_key=True) # No need primary key
    primary_school = models.ForeignKey(School, related_name="prim_school", null=True, blank=True)
    secondary_school = models.ForeignKey(School, related_name="second_school", null=True, blank=True)


class OneTime(AbstractDataTimeType, AbstractLifeTime):
    """Has start_date, start_time, end_date, end_time"""

    ONETIME_DATETIME = 0
    ONETIME_PERIOD = 1
    STOP_TYPES = (
        (ONETIME_DATETIME, _('Date/Time')),
        (ONETIME_PERIOD, _('Period')),
    )
    # onetime_id = models.AutoField(primary_key=True)
    stop_type = models.PositiveSmallIntegerField(choices=STOP_TYPES, default=0)
    start_datetime = models.DateTimeField(default=datetime.now, blank=True, null=True)
    stop_datetime = models.DateTimeField(default=datetime.now, blank=True, null=True)

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


class SpecificDateTime(AbstractDataTimeType, AbstractLifeTime, AbstractSpecificDateTime):
    """Specific Date Time
    """
    # spec_date_time_id = models.AutoField(primary_key=True)
    pass


# class AbstractMonths(models.Model):
#     """Split Month to be an abstract class. Do modular
#     """
#     import calendar
#     MONTHS = (
#         (calendar.month_abbr[1], _(calendar.month_abbr[1])),
#         (calendar.month_abbr[2], _(calendar.month_abbr[2])),
#         (calendar.month_abbr[3], _(calendar.month_abbr[3])),
#         (calendar.month_abbr[4], _(calendar.month_abbr[4])),
#         (calendar.month_abbr[5], _(calendar.month_abbr[5])),
#         (calendar.month_abbr[6], _(calendar.month_abbr[6])),
#         (calendar.month_abbr[7], _(calendar.month_abbr[7])),
#         (calendar.month_abbr[8], _(calendar.month_abbr[8])),
#         (calendar.month_abbr[9], _(calendar.month_abbr[9])),
#         (calendar.month_abbr[10], _(calendar.month_abbr[10])),
#         (calendar.month_abbr[11], _(calendar.month_abbr[11])),
#         (calendar.month_abbr[12], _(calendar.month_abbr[12])),
#     )
#     # abstract_month_id = models.AutoField(primary_key=True)
#     month = models.SmallIntegerField(default=datetime.today().month)
#
#     class Meta:
#         abstract = True
