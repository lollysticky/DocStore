# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-19 08:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_auto_20161016_1026'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='labels',
            field=models.ManyToManyField(to='backend.Label'),
        ),
        migrations.AddField(
            model_name='project',
            name='labels',
            field=models.ManyToManyField(to='backend.Label'),
        ),
        migrations.AlterField(
            model_name='document',
            name='type',
            field=models.IntegerField(choices=[(0, b'unknown'), (1, b'pdf'), (2, b'docx'), (3, b'img')], default=0, max_length=12),
        ),
    ]
