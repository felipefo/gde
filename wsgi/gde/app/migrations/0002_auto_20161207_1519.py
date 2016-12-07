# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuantidadeAcumulada',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('quantidade', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='TipoAcumulo',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('nome', models.CharField(null=True, max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='tipologia',
            name='fimAcumulo',
            field=models.IntegerField(default=2016),
        ),
        migrations.AlterField(
            model_name='tipologia',
            name='inicioAcumulo',
            field=models.IntegerField(default=1970),
        ),
        migrations.RemoveField(
            model_name='tipologia',
            name='quantidadeAcumulada',
        ),
        migrations.AddField(
            model_name='quantidadeacumulada',
            name='tipoAcumulo',
            field=models.ManyToManyField(to='app.TipoAcumulo', related_name='tipoAcumulo'),
        ),
        migrations.AddField(
            model_name='tipologia',
            name='quantidadeAcumulada',
            field=models.ManyToManyField(to='app.QuantidadeAcumulada', related_name='quantidadeAcumulada'),
        ),
    ]
