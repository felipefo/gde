# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20161024_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setor',
            name='historico',
            field=models.CharField(null=True, unique=True, max_length=250, blank=True),
        ),
    ]
