# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leave', '0006_assignleave'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assignleave',
            name='employee',
        ),
        migrations.DeleteModel(
            name='AssignLeave',
        ),
    ]
