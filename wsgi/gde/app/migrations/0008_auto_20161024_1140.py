# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20161020_1422'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='setor',
            name='atividade',
        ),
        migrations.AddField(
            model_name='setor',
            name='atividade',
            field=models.ManyToManyField(null=True, to='app.Atividade'),
        ),
        migrations.RemoveField(
            model_name='setor',
            name='historico',
        ),
        migrations.AddField(
            model_name='setor',
            name='historico',
            field=models.ManyToManyField(null=True, to='app.Historico'),
        ),
    ]
