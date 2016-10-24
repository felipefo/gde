# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20161024_1519'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='setor',
            name='atividade',
        ),
        migrations.AddField(
            model_name='setor',
            name='atividade',
            field=models.ForeignKey(to='app.Atividade', null=True),
        ),
    ]
