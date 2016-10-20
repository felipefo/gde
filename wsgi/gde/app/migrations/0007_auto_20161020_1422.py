# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20161020_1406'),
    ]

    operations = [
        migrations.CreateModel(
            name='Atividade',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descricao', models.TextField(null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Historico',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=20, null=True, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='setor',
            name='atividade',
            field=models.ForeignKey(to='app.Atividade', null=True),
        ),
        migrations.AddField(
            model_name='setor',
            name='historico',
            field=models.ForeignKey(to='app.Historico', null=True),
        ),
    ]
