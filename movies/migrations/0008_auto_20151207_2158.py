# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0007_cast_person'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cast',
            name='movie_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='cast',
            name='person_id',
            field=models.IntegerField(default=0, db_index=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='person_id',
            field=models.IntegerField(serialize=False, primary_key=True),
        ),
    ]
