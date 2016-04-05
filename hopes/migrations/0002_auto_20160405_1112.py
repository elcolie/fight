# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hopes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='primary_school',
            field=models.ForeignKey(blank=True, related_name='prim_school', to='hopes.School', null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='secondary_school',
            field=models.ForeignKey(blank=True, related_name='second_school', to='hopes.School', null=True),
        ),
    ]
