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
    Abstract base classes for
    """
    address = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    postcode = models.CharField(max=20)
    country = models.CharField(max_length=46)
    build_date = models.DateField(_("Date"), default=datetime.date.today)

    class Meta:
        abstract = True


class School(Building):
    name = models.CharField(max_lenght=255)


class Student(HumanProfile):
    primary_school = models.ForeignKey(School)
    secondary_school = models.ForeignKey(School)








