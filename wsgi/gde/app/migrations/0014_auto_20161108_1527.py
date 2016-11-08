# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_auto_20161024_1543'),
    ]

    operations = [
        migrations.CreateModel(
            name='Elemento',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('nome', models.CharField(unique=True, max_length=60, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Fase',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('nome', models.CharField(unique=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FormaDocumental',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('nome', models.CharField(unique=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('nome', models.CharField(unique=True, max_length=60, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Opcao',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('nome', models.CharField(unique=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RestricaoAcesso',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('descricao', models.CharField(unique=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Suporte',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('nome', models.CharField(unique=True, max_length=60, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tipologia',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('finalidade', models.TextField(unique=True, null=True)),
                ('nome', models.CharField(unique=True, max_length=50, null=True)),
                ('identificação', models.CharField(unique=True, max_length=50, null=True)),
                ('inicioAcumulo', models.DateField(null=True)),
                ('fimAcumulo', models.DateField(null=True)),
                ('quantidadeAcumulada', models.CharField(unique=True, max_length=50, null=True)),
                ('embasamentoLegal', models.CharField(unique=True, max_length=50, null=True)),
                ('anexo', models.ForeignKey(to='app.Opcao', related_name='anexo', null=True)),
                ('atividade', models.ForeignKey(to='app.Atividade', related_name='atividade', null=True)),
                ('elemento', models.ManyToManyField(to='app.Elemento', related_name='elemento')),
                ('especieDocumental', models.ForeignKey(to='app.EspecieDocumental', related_name='especieDocumental', null=True)),
                ('fase', models.ManyToManyField(to='app.Fase')),
                ('formaDocumental', models.ForeignKey(to='app.FormaDocumental', related_name='formaDocumental', null=True)),
                ('genero', models.ManyToManyField(to='app.Genero', related_name='genero')),
                ('informacaoOutrosDocumentos', models.ForeignKey(to='app.Opcao', related_name='informacaoOutrosDocumentos', null=True)),
                ('relacaoExterna', models.ForeignKey(to='app.Opcao', related_name='relacaoExterna', null=True)),
                ('relacaoInterna', models.ForeignKey(to='app.Opcao', related_name='relacaoInterna', null=True)),
                ('restricaoAcesso', models.ManyToManyField(to='app.RestricaoAcesso', related_name='restricaoAcesso')),
                ('riscoPerda', models.ForeignKey(to='app.Opcao', related_name='riscoPerda', null=True)),
                ('setor', models.ForeignKey(to='app.Setor', related_name='setor', null=True)),
                ('suporte', models.ForeignKey(to='app.Suporte', related_name='suporte', null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='lotacao',
            new_name='setor',
        ),
        migrations.AddField(
            model_name='tipologia',
            name='usuario',
            field=models.ForeignKey(to='app.Usuario', related_name='usuario', null=True),
        ),
    ]
