# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-16 14:11
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('drf_fcm', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='device',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
    ]
