# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leave', '0004_auto_20150702_0451'),
    ]

    operations = [
        migrations.AddField(
            model_name='leave',
            name='status',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
