# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leave', '0002_auto_20150702_0402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leave',
            name='from_date',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='leave',
            name='to_date',
            field=models.DateField(null=True, blank=True),
        ),
    ]
