# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-03-23 10:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='calendarcontent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.TextField(blank=True, help_text='Name', null=True, verbose_name='Name')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.TextField(blank=True, help_text='Artist', null=True, verbose_name='Artist')),
                ('notes', models.TextField(blank=True, help_text='Notes', null=True, verbose_name='Notes')),
                ('day', models.DateField(help_text='Day of the event', verbose_name='Day of the event')),
                ('start_time', models.TimeField(help_text='Starting time', verbose_name='Starting time')),
                ('end_time', models.TimeField(help_text='Final time', verbose_name='Final time')),
                ('hall', models.TextField(blank=True, help_text='Hall', null=True, verbose_name='Hall')),
                ('image', models.ImageField(upload_to='images')),
            ],
            options={
                'verbose_name': 'Scheduling',
                'verbose_name_plural': 'Scheduling',
            },
        ),
    ]
