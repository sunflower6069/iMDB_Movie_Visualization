# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_auto_20151119_2215'),
    ]

    operations = [
        migrations.CreateModel(
            name='genres',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('movie_id', models.IntegerField(default=0)),
                ('genre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='titles',
            fields=[
                ('movie_id', models.IntegerField(serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=200)),
            ],
        ),
    ]
