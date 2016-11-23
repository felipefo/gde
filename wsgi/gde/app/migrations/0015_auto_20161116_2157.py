# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_auto_20161108_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setor',
            name='campus',
            field=models.ForeignKey(null=True, verbose_name='Campus', to='app.Campus'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='setor',
            field=models.ForeignKey(null=True, verbose_name='Setor', to='app.Setor'),
        ),
    ]
