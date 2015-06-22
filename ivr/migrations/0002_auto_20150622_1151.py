# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ivr', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ivrdata',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 22, 11, 51, 38, 347891, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ivrdata',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 22, 11, 51, 44, 595876, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
