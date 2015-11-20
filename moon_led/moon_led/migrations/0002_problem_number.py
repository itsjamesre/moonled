# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moon_led', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='number',
            field=models.PositiveSmallIntegerField(default=0),
            preserve_default=False,
        ),
    ]
