# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-08 10:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myCommServer', '0003_mycommdevice_mycommmsg'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usermsg',
            old_name='receivedDate',
            new_name='receivedTime',
        ),
    ]
