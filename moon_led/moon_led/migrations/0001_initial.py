# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('grade', models.CharField(max_length=4)),
                ('start', models.CharField(max_length=100)),
                ('path', models.CharField(max_length=100)),
                ('finish', models.CharField(max_length=100)),
            ],
        ),
    ]
