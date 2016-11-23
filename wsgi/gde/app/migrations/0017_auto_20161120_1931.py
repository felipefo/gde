# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_auto_20161120_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setor',
            name='funcao',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='setor',
            name='nome',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='setor',
            name='sigla',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
