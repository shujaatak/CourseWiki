# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-10 12:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0007_delete_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='first_name',
            field=models.CharField(default='Name not submitted', max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='public_profile',
            field=models.CharField(default='about:blank', max_length=2000),
            preserve_default=False,
        ),
    ]
