# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0007_auto_20150707_0727'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='leave_taken',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
