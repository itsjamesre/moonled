# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moon_led', '0002_problem_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='name',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='problem',
            name='setter',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
