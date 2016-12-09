# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20161209_1704'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tipologia',
            name='riscoPerda',
        ),
        migrations.AlterField(
            model_name='tipologia',
            name='identificacao',
            field=models.CharField(max_length=50, null=True, unique=True),
        ),
    ]
