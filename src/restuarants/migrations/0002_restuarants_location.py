# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-15 07:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restuarants', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='restuarants',
            name='location',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
