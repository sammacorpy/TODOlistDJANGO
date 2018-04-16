# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='todo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=40)),
                ('desc', models.CharField(max_length=200)),
                ('complete', models.BooleanField(default=False)),
                ('suspended', models.BooleanField(default=False)),
            ],
        ),
    ]
