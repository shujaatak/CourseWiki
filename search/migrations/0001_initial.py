# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-25 21:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Syllabus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('syllabus_name', models.CharField(max_length=250, unique=True)),
                ('syllabus_path', models.CharField(max_length=250)),
                ('syllabus_reviews', models.CharField(max_length=300)),
                ('syllabus_technologies', models.CharField(max_length=300)),
            ],
        ),
    ]
