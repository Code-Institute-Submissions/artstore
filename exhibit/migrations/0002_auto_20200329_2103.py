# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-03-29 21:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exhibit', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='galleryart',
            options={'verbose_name_plural': 'Art'},
        ),
        migrations.AlterModelOptions(
            name='galleryartist',
            options={'verbose_name_plural': 'Artists'},
        ),
    ]
