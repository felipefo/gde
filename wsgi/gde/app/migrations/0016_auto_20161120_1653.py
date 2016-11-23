# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_auto_20161116_2157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setor',
            name='historico',
            field=models.CharField(max_length=250, null=True, blank=True),
        ),
    ]
