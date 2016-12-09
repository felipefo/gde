# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20161207_1555'),
    ]

    operations = [
        migrations.AddField(
            model_name='tipologia',
            name='quantidadeVias',
            field=models.BooleanField(default=True, choices=[(True, 'Sim'), (False, 'Não')]),
        ),
    ]
