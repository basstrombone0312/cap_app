# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-27 04:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('packet_vis', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Packets',
            new_name='Packet',
        ),
    ]
