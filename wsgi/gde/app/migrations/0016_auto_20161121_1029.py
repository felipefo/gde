# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_auto_20161110_1642'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tipologia',
            name='anexo',
        ),
        migrations.AddField(
            model_name='tipologia',
            name='anexo',
            field=models.ManyToManyField(related_name='anexo', to='app.Opcao'),
        ),
        migrations.RemoveField(
            model_name='tipologia',
            name='informacaoOutrosDocumentos',
        ),
        migrations.AddField(
            model_name='tipologia',
            name='informacaoOutrosDocumentos',
            field=models.ManyToManyField(related_name='informacaoOutrosDocumentos', to='app.Opcao'),
        ),
        migrations.RemoveField(
            model_name='tipologia',
            name='relacaoExterna',
        ),
        migrations.AddField(
            model_name='tipologia',
            name='relacaoExterna',
            field=models.ManyToManyField(related_name='relacaoExterna', to='app.Opcao'),
        ),
        migrations.RemoveField(
            model_name='tipologia',
            name='relacaoInterna',
        ),
        migrations.AddField(
            model_name='tipologia',
            name='relacaoInterna',
            field=models.ManyToManyField(related_name='relacaoInterna', to='app.Opcao'),
        ),
        migrations.RemoveField(
            model_name='tipologia',
            name='riscoPerda',
        ),
        migrations.AddField(
            model_name='tipologia',
            name='riscoPerda',
            field=models.ManyToManyField(related_name='riscoPerda', to='app.Opcao'),
        ),
    ]
