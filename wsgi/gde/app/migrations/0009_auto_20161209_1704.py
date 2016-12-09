# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20161209_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipologia',
            name='embasamentoLegal',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='tipologia',
            name='finalidade',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='tipologia',
            name='identificacao',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
