# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-10 21:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SignUp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=254)),
                ('email', models.EmailField(max_length=254)),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Date inscription')),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
