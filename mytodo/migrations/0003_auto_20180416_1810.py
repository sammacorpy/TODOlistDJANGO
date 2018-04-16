# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('mytodo', '0002_todo_lastdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='lastdate',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 16, 18, 10, 42, 858119), blank=True),
        ),
    ]
