# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-01 12:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Trip', '0004_plan_daycount'),
    ]

    operations = [
        migrations.AddField(
            model_name='tripmain',
            name='TotalDay',
            field=models.IntegerField(blank=True, default=1),
        ),
    ]