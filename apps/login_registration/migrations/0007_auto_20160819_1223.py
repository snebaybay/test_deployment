# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-19 16:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_registration', '0006_auto_20160819_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='task_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='task_time',
            field=models.TimeField(),
        ),
    ]