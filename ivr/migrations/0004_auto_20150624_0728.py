# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('ivr', '0003_ivrdata_ivr_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ivrdata',
            name='user',
            field=models.ForeignKey(related_name='site_Ivruser', to=settings.AUTH_USER_MODEL),
        ),
    ]
