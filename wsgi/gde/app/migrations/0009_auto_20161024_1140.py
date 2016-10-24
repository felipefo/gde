# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20161024_1140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setor',
            name='atividade',
            field=models.ManyToManyField(to='app.Atividade'),
        ),
        migrations.AlterField(
            model_name='setor',
            name='historico',
            field=models.ManyToManyField(to='app.Historico'),
        ),
    ]
