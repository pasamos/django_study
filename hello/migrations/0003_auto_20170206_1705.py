# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-06 09:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0002_auto_20170206_1652'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='userinfo',
            table='hello_userinfo',
        ),
    ]
