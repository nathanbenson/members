# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2022-05-17 23:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscribers', '0005_auto_20220517_2344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriber',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]