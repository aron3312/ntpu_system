# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-25 10:43
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0030_auto_20171024_2258'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student_data',
            options={'permissions': (('can_read', 'can read'),)},
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 25, 10, 43, 17, 445731, tzinfo=utc)),
        ),
    ]
