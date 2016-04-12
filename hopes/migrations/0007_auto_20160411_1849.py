# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hopes', '0006_auto_20160411_1845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='onetime',
            name='lifetime_quantity',
            field=models.PositiveIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='onetime',
            name='lifetime_unit',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(0, 'Stop every minutes'), (1, 'Stop every hour'), (2, 'Stop every day'), (3, 'Stop every month'), (4, 'Stop every year'), (5, 'NonStop')], default=0),
        ),
    ]
