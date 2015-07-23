# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0006_auto_20150707_0707'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignleave',
            name='sums',
            field=models.IntegerField(default=0, db_column=b'get_count'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='assignleave',
            name='employee',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
