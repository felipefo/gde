# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_auto_20161108_1527'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tipologia',
            old_name='fase',
            new_name='fases',
        ),
        migrations.RenameField(
            model_name='tipologia',
            old_name='identificação',
            new_name='identificacao',
        ),
    ]
