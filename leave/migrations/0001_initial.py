# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Leave',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('leave_type', models.CharField(max_length=10, choices=[(b'select', b'Select a leave type'), (b'casual', b'Casual Leave'), (b'sick', b'Sick Leave'), (b'optional', b'Optional leave')])),
                ('from_date', models.DateField(null=True, blank=True)),
                ('to_date', models.DateField(null=True, blank=True)),
                ('comment', models.CharField(max_length=100)),
                ('employee', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
