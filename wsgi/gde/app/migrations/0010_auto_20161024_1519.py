# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20161024_1140'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='campussetor',
            name='campus',
        ),
        migrations.RemoveField(
            model_name='campussetor',
            name='setor',
        ),
        migrations.RemoveField(
            model_name='campus',
            name='setores',
        ),
        migrations.AddField(
            model_name='setor',
            name='campus',
            field=models.ForeignKey(null=True, to='app.Campus'),
        ),
        migrations.RemoveField(
            model_name='setor',
            name='historico',
        ),
        migrations.AddField(
            model_name='setor',
            name='historico',
            field=models.CharField(null=True, max_length=250, unique=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='lotacao',
            field=models.ForeignKey(null=True, to='app.Setor'),
        ),
        migrations.DeleteModel(
            name='CampusSetor',
        ),
        migrations.DeleteModel(
            name='Historico',
        ),
    ]
