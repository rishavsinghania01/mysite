# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-08 09:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20180208_1428'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Doctor',
        ),
        migrations.AlterField(
            model_name='acceptor',
            name='a1',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='acceptor',
            name='a2',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='acceptor',
            name='a3',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='acceptor',
            name='a4',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='acceptor',
            name='a5',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='acceptor',
            name='a6',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
