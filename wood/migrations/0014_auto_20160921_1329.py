# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-21 10:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wood', '0013_auto_20160921_1233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='email',
            field=models.CharField(max_length=100),
        ),
    ]