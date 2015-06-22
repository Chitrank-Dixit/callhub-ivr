# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ivr', '0002_auto_20150622_1151'),
    ]

    operations = [
        migrations.AddField(
            model_name='ivrdata',
            name='ivr_name',
            field=models.CharField(default=datetime.datetime(2015, 6, 22, 18, 9, 37, 550958, tzinfo=utc), max_length=120),
            preserve_default=False,
        ),
    ]
