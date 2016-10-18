# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_campus'),
    ]

    operations = [
        migrations.AddField(
            model_name='campus',
            name='setores',
            field=models.ManyToManyField(to='app.Setor'),
        ),
    ]
