# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-01-13 10:26
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('faraz', '0002_auto_20170113_0218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]