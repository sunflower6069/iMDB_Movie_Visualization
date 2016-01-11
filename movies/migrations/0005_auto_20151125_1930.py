# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_genres_titles'),
    ]

    operations = [
        migrations.CreateModel(
            name='ratings',
            fields=[
                ('movie_id', models.IntegerField(serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('rating', models.FloatField(default=0)),
            ],
        ),
        migrations.DeleteModel(
            name='titles',
        ),
    ]
