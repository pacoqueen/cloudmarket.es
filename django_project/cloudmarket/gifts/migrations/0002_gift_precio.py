# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gifts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gift',
            name='precio',
            field=models.FloatField(default=None),
            preserve_default=True,
        ),
    ]
