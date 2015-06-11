# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gifts', '0004_auto_20150611_0436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='notes',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='item',
            name='photo',
            field=models.ImageField(upload_to=b'img', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='item',
            name='url',
            field=models.URLField(blank=True),
            preserve_default=True,
        ),
    ]
