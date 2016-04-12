# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('hopes', '0003_onetime_recurrencetime_specdatetime'),
    ]

    operations = [
        migrations.CreateModel(
            name='AbstractDataTimeType',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('schedule_category', models.CharField(default=0, max_length=30, choices=[(0, 'One-Time type'), (1, 'Recurrence type'), (2, 'Specific date time type')])),
            ],
        ),
        migrations.DeleteModel(
            name='RecurrenceTime',
        ),
        migrations.DeleteModel(
            name='SpecDateTime',
        ),
        migrations.RemoveField(
            model_name='onetime',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='onetime',
            name='end_time',
        ),
        migrations.RemoveField(
            model_name='onetime',
            name='id',
        ),
        migrations.RemoveField(
            model_name='onetime',
            name='period',
        ),
        migrations.RemoveField(
            model_name='onetime',
            name='start_date',
        ),
        migrations.RemoveField(
            model_name='onetime',
            name='start_time',
        ),
        migrations.RemoveField(
            model_name='onetime',
            name='type',
        ),
        migrations.AddField(
            model_name='onetime',
            name='start_datetime',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='onetime',
            name='stop_datetime',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='onetime',
            name='stop_type',
            field=models.CharField(default=0, max_length=10, choices=[(0, 'Date/Time type'), (1, 'Life time min, hr, day, month, forever')]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='school',
            name='build_date',
            field=models.DateField(default=datetime.datetime.today, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='student',
            name='birthDate',
            field=models.DateField(default=datetime.datetime.today, verbose_name='Date'),
        ),
        migrations.AddField(
            model_name='onetime',
            name='abstractdatatimetype_ptr',
            field=models.OneToOneField(default=1, primary_key=True, serialize=False, auto_created=True, parent_link=True, to='hopes.AbstractDataTimeType'),
            preserve_default=False,
        ),
    ]
