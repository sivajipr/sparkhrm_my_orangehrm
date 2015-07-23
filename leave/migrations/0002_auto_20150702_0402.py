# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leave', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leave',
            name='from_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='leave',
            name='leave_type',
            field=models.CharField(max_length=10, choices=[(b'casual', b'Casual Leave'), (b'sick', b'Sick Leave'), (b'optional', b'Optional leave')]),
        ),
        migrations.AlterField(
            model_name='leave',
            name='to_date',
            field=models.DateField(),
        ),
    ]
