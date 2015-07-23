# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leave', '0003_auto_20150702_0447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leave',
            name='comment',
            field=models.TextField(max_length=100),
        ),
    ]
