# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-08 04:59
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('search', '0004_project_project_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('public_profile', models.CharField(max_length=1000)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True)),
            ],
        ),
    ]