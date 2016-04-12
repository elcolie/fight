# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hopes', '0005_auto_20160411_0854'),
    ]

    operations = [
        migrations.AddField(
            model_name='onetime',
            name='lifetime_quantity',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='onetime',
            name='lifetime_unit',
            field=models.PositiveSmallIntegerField(default=0, choices=[(0, 'Stop every minutes'), (1, 'Stop every hour'), (2, 'Stop every day'), (3, 'Stop every month'), (4, 'Stop every year'), (5, 'NonStop')]),
        ),
        migrations.AlterField(
            model_name='onetime',
            name='stop_type',
            field=models.PositiveSmallIntegerField(default=0, choices=[(0, 'Date/Time'), (1, 'Period')]),
        ),
    ]
