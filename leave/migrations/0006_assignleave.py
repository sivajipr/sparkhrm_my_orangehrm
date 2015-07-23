# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('leave', '0005_leave_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssignLeave',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('casual', models.IntegerField(default=0)),
                ('sick', models.IntegerField(default=0)),
                ('optional', models.IntegerField(default=1)),
                ('employee', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
