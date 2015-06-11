# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gifts', '0003_person_fecha_nacimiento'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gift',
            old_name='precio',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='person',
            old_name='fecha_nacimiento',
            new_name='birthdate',
        ),
        migrations.RenameField(
            model_name='person',
            old_name='nombre',
            new_name='name',
        ),
    ]
