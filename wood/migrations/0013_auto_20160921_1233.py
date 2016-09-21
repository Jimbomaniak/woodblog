# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-21 09:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wood', '0012_auto_20160921_0952'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='email',
            field=models.CharField(default='ex@ex.com', max_length=100),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='address',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]