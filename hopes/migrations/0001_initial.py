# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('address', models.CharField(max_length=255)),
                ('region', models.CharField(max_length=255)),
                ('postcode', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=46)),
                ('build_date', models.DateField(verbose_name='Date', default=datetime.date.today)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('surname', models.CharField(max_length=512)),
                ('country', models.CharField(max_length=46)),
                ('birthDate', models.DateField(verbose_name='Date', default=datetime.date.today)),
                ('weight_kg', models.PositiveSmallIntegerField(default=1)),
                ('blood', models.CharField(choices=[('A', 'A-type'), ('B', 'B-type'), ('AB', 'AB-type'), ('O', 'O-type')], max_length=2)),
                ('height_cm', models.SmallIntegerField(default=1)),
                ('primary_school', models.ForeignKey(to='hopes.School', related_name='prim_school')),
                ('secondary_school', models.ForeignKey(to='hopes.School', related_name='second_school')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
