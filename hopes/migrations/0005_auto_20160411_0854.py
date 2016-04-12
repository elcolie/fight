# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hopes', '0004_auto_20160411_0841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abstractdatatimetype',
            name='schedule_category',
            field=models.IntegerField(choices=[(0, 'One-Time type'), (1, 'Recurrence type'), (2, 'Specific date time type')], default=0),
        ),
        migrations.AlterField(
            model_name='onetime',
            name='stop_type',
            field=models.IntegerField(choices=[(0, 'Date/Time type'), (1, 'Life time min, hr, day, month, forever')], default=0),
        ),
    ]
