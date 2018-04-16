# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mytodo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='lastdate',
            field=models.CharField(default=datetime.datetime(2018, 4, 16, 18, 8, 3, 327778, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
    ]
