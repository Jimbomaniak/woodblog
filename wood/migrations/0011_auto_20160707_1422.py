# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-07 11:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wood', '0010_auto_20160707_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='comment',
            field=models.TextField(blank=True, verbose_name='Дополнительная информация'),
        ),
    ]
