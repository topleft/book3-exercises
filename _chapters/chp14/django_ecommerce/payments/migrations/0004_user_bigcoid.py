# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-01-02 17:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0003_initial_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='bigCoID',
            field=models.CharField(default='foo', max_length=50),
            preserve_default=False,
        ),
    ]