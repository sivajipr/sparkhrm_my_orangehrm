# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0008_profile_leave_taken'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='leave_taken',
        ),
    ]
