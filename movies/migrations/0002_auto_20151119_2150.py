# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='dates',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('movie_id', models.IntegerField(default=0)),
                ('date', models.DateTimeField(verbose_name=b'date published')),
            ],
        ),
        migrations.RemoveField(
            model_name='actor',
            name='movie',
        ),
        migrations.RemoveField(
            model_name='actor',
            name='person',
        ),
        migrations.RemoveField(
            model_name='director',
            name='movie',
        ),
        migrations.RemoveField(
            model_name='director',
            name='person',
        ),
        migrations.RemoveField(
            model_name='rating',
            name='movie',
        ),
        migrations.DeleteModel(
            name='Actor',
        ),
        migrations.DeleteModel(
            name='Director',
        ),
        migrations.DeleteModel(
            name='Movie',
        ),
        migrations.DeleteModel(
            name='Person',
        ),
        migrations.DeleteModel(
            name='Rating',
        ),
    ]
