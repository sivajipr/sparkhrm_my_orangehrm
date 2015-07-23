# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_profile_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='status',
            field=models.CharField(default=b'single', max_length=10, choices=[(b'single', b'Single'), (b'married', b'Married'), (b'other', b'Others')]),
            preserve_default=True,
        ),
    ]
