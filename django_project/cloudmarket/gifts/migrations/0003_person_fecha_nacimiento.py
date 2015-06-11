# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gifts', '0002_gift_precio'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='fecha_nacimiento',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
