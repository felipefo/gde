# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Atividade',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('descricao', models.TextField(unique=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Campus',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('nome', models.CharField(max_length=30, unique=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Elemento',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('nome', models.CharField(max_length=60, unique=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EspecieDocumental',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('nome', models.CharField(max_length=20, unique=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Fase',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('nome', models.CharField(max_length=20, unique=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FormaDocumental',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('nome', models.CharField(max_length=20, unique=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('nome', models.CharField(max_length=60, unique=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Opcao',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('nome', models.CharField(max_length=20, unique=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RestricaoAcesso',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('descricao', models.CharField(max_length=200, unique=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Setor',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('nome', models.CharField(max_length=20, null=True)),
                ('sigla', models.CharField(max_length=20, null=True)),
                ('funcao', models.CharField(max_length=250, null=True)),
                ('historico', models.CharField(max_length=250, null=True, blank=True)),
                ('campus', models.ForeignKey(verbose_name='Campus', null=True, to='app.Campus')),
            ],
        ),
        migrations.CreateModel(
            name='Suporte',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('nome', models.CharField(max_length=60, unique=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tipologia',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('finalidade', models.TextField(unique=True, null=True)),
                ('nome', models.CharField(max_length=50, unique=True, null=True)),
                ('identificacao', models.CharField(max_length=50, unique=True, null=True)),
                ('inicioAcumulo', models.DateField(null=True)),
                ('fimAcumulo', models.DateField(null=True)),
                ('quantidadeAcumulada', models.CharField(max_length=50, unique=True, null=True)),
                ('embasamentoLegal', models.CharField(max_length=50, unique=True, null=True)),
                ('sugestao', models.TextField(unique=True, null=True)),
                ('anexo', models.ManyToManyField(related_name='anexo', to='app.Opcao')),
                ('atividade', models.ForeignKey(related_name='atividade', null=True, to='app.Atividade')),
                ('elemento', models.ManyToManyField(related_name='elemento', to='app.Elemento')),
                ('especieDocumental', models.ForeignKey(related_name='especieDocumental', null=True, to='app.EspecieDocumental')),
                ('fases', models.ManyToManyField(to='app.Fase')),
                ('formaDocumental', models.ForeignKey(related_name='formaDocumental', null=True, to='app.FormaDocumental')),
                ('genero', models.ManyToManyField(related_name='genero', to='app.Genero')),
                ('informacaoOutrosDocumentos', models.ManyToManyField(related_name='informacaoOutrosDocumentos', to='app.Opcao')),
                ('relacaoExterna', models.ManyToManyField(related_name='relacaoExterna', to='app.Opcao')),
                ('relacaoInterna', models.ManyToManyField(related_name='relacaoInterna', to='app.Opcao')),
                ('restricaoAcesso', models.ManyToManyField(related_name='restricaoAcesso', to='app.RestricaoAcesso')),
                ('riscoPerda', models.ManyToManyField(related_name='riscoPerda', to='app.Opcao')),
                ('setor', models.ForeignKey(related_name='setor', null=True, to='app.Setor')),
                ('suporte', models.ForeignKey(related_name='suporte', null=True, to='app.Suporte')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('setor', models.ForeignKey(verbose_name='Setor', null=True, to='app.Setor')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='tipologia',
            name='usuario',
            field=models.ForeignKey(related_name='usuario', null=True, to='app.Usuario'),
        ),
        migrations.AddField(
            model_name='atividade',
            name='setor',
            field=models.ForeignKey(null=True, to='app.Setor'),
        ),
    ]
