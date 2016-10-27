# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_auto_20161024_1543'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='lotacao',
            new_name='setor',
        ),
        migrations.AddField(
            model_name='usuario',
            name='campus',
            field=models.ForeignKey(null=True, to='app.Campus'),
        ),
    ]
