# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20151119_2150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dates',
            name='date',
            field=models.CharField(max_length=50),
        ),
    ]
