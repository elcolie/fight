# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('hopes', '0007_auto_20160411_1849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='onetime',
            name='lifetime_quantity',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='onetime',
            name='lifetime_unit',
            field=models.PositiveSmallIntegerField(blank=True, null=True, default=0, choices=[(0, 'Stop every minutes'), (1, 'Stop every hour'), (2, 'Stop every day'), (3, 'Stop every month'), (4, 'Stop every year'), (5, 'NonStop')]),
        ),
        migrations.AlterField(
            model_name='onetime',
            name='start_datetime',
            field=models.DateTimeField(blank=True, null=True, default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='onetime',
            name='stop_datetime',
            field=models.DateTimeField(blank=True, null=True, default=datetime.datetime.now),
        ),
    ]
