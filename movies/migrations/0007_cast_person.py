# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0006_auto_20151205_1628'),
    ]

    operations = [
        migrations.CreateModel(
            name='cast',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('movie_id', models.IntegerField(default=0, db_index=True)),
                ('person_id', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='person',
            fields=[
                ('person_id', models.IntegerField(serialize=False, primary_key=True, db_index=True)),
                ('name', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=10)),
            ],
        ),
    ]
