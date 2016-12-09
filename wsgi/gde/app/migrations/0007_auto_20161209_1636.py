# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_tipologia_quantidadevias'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tipologia',
            name='tipoAcumulo',
        ),
        migrations.AddField(
            model_name='tipologia',
            name='tipoAcumulo',
            field=models.ForeignKey(null=True, to='app.TipoAcumulo', related_name='tipoAcumulo'),
        ),
    ]
