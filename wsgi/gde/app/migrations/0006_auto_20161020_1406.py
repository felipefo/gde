# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_campus_setores'),
    ]

    operations = [
        migrations.CreateModel(
            name='CampusSetor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('campus', models.ForeignKey(to='app.Campus')),
                ('setor', models.ForeignKey(to='app.Setor')),
            ],
        ),
        migrations.AlterField(
            model_name='usuario',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='usuario',
            name='lotacao',
            field=models.ForeignKey(to='app.CampusSetor', null=True),
        ),
    ]
