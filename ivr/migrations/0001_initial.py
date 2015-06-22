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
            name='IvrData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ivr_message', models.CharField(max_length=500)),
                ('ivr_no_input_message', models.TextField(max_length=500)),
                ('ivr_wrong_input_message', models.TextField(max_length=500)),
                ('ip_zero', models.CharField(max_length=500)),
                ('ip_one', models.CharField(max_length=500)),
                ('ip_two', models.CharField(max_length=500)),
                ('ip_three', models.CharField(max_length=500)),
                ('ip_four', models.CharField(max_length=500)),
                ('ip_five', models.CharField(max_length=500)),
                ('ip_six', models.CharField(max_length=500)),
                ('ip_seven', models.CharField(max_length=500)),
                ('ip_eight', models.CharField(max_length=500)),
                ('ip_nine', models.CharField(max_length=500)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
