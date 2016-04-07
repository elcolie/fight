# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hopes', '0002_auto_20160405_1112'),
    ]

    operations = [
        migrations.CreateModel(
            name='OneTime',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('start_date', models.DateField(blank=True)),
                ('start_time', models.TimeField(blank=True)),
                ('end_date', models.DateField(blank=True)),
                ('end_time', models.TimeField(blank=True)),
                ('period', models.CharField(choices=[('Min', 'Stop every minutes'), ('Hour', 'Stop every hour'), ('Day', 'Stop every day'), ('Month', 'Stop every month'), ('Year', 'Stop every year'), ('Forever', 'Not start again')], max_length=10)),
                ('type', models.CharField(choices=[('Date', 'Date/Time type'), ('Period', 'Life time min, hr, day, month, forever')], max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RecurrenceTime',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('start_date', models.DateField(blank=True)),
                ('start_time', models.TimeField(blank=True)),
                ('end_date', models.DateField(blank=True)),
                ('end_time', models.TimeField(blank=True)),
                ('period', models.CharField(choices=[('Min', 'Stop every minutes'), ('Hour', 'Stop every hour'), ('Day', 'Stop every day'), ('Month', 'Stop every month'), ('Year', 'Stop every year'), ('Forever', 'Not start again')], max_length=10)),
                ('monday', models.BooleanField(default=False)),
                ('tuesday', models.BooleanField(default=False)),
                ('wednesday', models.BooleanField(default=False)),
                ('thursday', models.BooleanField(default=False)),
                ('friday', models.BooleanField(default=False)),
                ('saturday', models.BooleanField(default=False)),
                ('sunday', models.BooleanField(default=False)),
                ('january', models.BooleanField(default=False)),
                ('february', models.BooleanField(default=False)),
                ('march', models.BooleanField(default=False)),
                ('april', models.BooleanField(default=False)),
                ('may', models.BooleanField(default=False)),
                ('june', models.BooleanField(default=False)),
                ('july', models.BooleanField(default=False)),
                ('august', models.BooleanField(default=False)),
                ('september', models.BooleanField(default=False)),
                ('october', models.BooleanField(default=False)),
                ('november', models.BooleanField(default=False)),
                ('december', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SpecDateTime',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('start_date', models.DateField(blank=True)),
                ('start_time', models.TimeField(blank=True)),
                ('end_date', models.DateField(blank=True)),
                ('end_time', models.TimeField(blank=True)),
                ('period', models.CharField(choices=[('Min', 'Stop every minutes'), ('Hour', 'Stop every hour'), ('Day', 'Stop every day'), ('Month', 'Stop every month'), ('Year', 'Stop every year'), ('Forever', 'Not start again')], max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
