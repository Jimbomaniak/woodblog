# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-21 06:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wood', '0011_auto_20160707_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='phone_num',
            field=models.CharField(max_length=13),
        ),
    ]