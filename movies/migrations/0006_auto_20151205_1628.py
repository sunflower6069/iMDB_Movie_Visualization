# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_auto_20151125_1930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dates',
            name='date',
            field=models.CharField(max_length=50, db_index=True),
        ),
        migrations.AlterField(
            model_name='genres',
            name='movie_id',
            field=models.IntegerField(default=0, db_index=True),
        ),
        migrations.AlterField(
            model_name='ratings',
            name='rating',
            field=models.FloatField(default=0, db_index=True),
        ),
    ]
