# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_profile_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='dob',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
