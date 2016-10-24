# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20161024_1531'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='setor',
            name='atividade',
        ),
        migrations.AddField(
            model_name='atividade',
            name='setor',
            field=models.ForeignKey(to='app.Setor', null=True),
        ),
    ]
