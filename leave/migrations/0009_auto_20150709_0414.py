# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leave', '0008_leave_leave_taken'),
    ]

    operations = [
        migrations.RenameField(
            model_name='leave',
            old_name='leave_taken',
            new_name='leave_days',
        ),
    ]
