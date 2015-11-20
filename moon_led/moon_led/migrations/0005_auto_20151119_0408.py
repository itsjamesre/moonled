# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moon_led', '0004_holdset_setup'),
    ]

    operations = [
        migrations.DeleteModel(
            name='HoldSet',
        ),
        migrations.DeleteModel(
            name='Setup',
        ),
        migrations.AddField(
            model_name='problem',
            name='hold_set',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='problem',
            name='setup',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
