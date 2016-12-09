# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20161209_1636'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tipologia',
            name='fases',
        ),
        migrations.AddField(
            model_name='tipologia',
            name='fases',
            field=models.ForeignKey(null=True, to='app.Fase', related_name='fases'),
        ),
    ]
