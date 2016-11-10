from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models


class EspecieDocumental(models.Model):
    nome = models.CharField(max_length=20, null=True, blank=False, unique=True)

    def __str__(self):
        return self.nome

class Campus(models.Model):
    nome = models.CharField(max_length=30, null=True, blank=False, unique=True)

    def __str__(self):
        return self.nome

class Setor(models.Model):
    campus = models.ForeignKey(Campus, null=True)
    nome = models.CharField(max_length=20, null=True, blank=False, unique=True)
    sigla = models.CharField(max_length=20, null=True, blank=False, unique=True)
    funcao = models.CharField(max_length=250, null=True, blank=False, unique=True)
    historico = models.CharField(max_length=250, null=True, blank=True, unique=True)

    def __str__(self):
        return self.nome

class Atividade(models.Model):
    setor = models.ForeignKey(Setor, null=True)
    descricao = models.TextField(null=True, blank=False, unique=True)

    def __str__(self):
        return self.descricao

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    setor = models.ForeignKey(Setor, null=True)

    def __str__(self):
        return self.user

class Opcao(models.Model):
    nome = models.CharField(max_length=20, null=True, blank=False, unique=True)

    def __str__(self):
        return self.nome

class Elemento(models.Model):
    nome = models.CharField(max_length=60, null=True, blank=False, unique=True)

    def __str__(self):
        return self.nome

class Suporte(models.Model):
    nome = models.CharField(max_length=60, null=True, blank=False, unique=True)

    def __str__(self):
        return self.nome

class Genero(models.Model):
    nome = models.CharField(max_length=60, null=True, blank=False, unique=True)

    def __str__(self):
        return self.nome

class RestricaoAcesso(models.Model):
    descricao = models.CharField(max_length=200, null=True, blank=False, unique=True)

    def __str__(self):
        return self.descricao

class FormaDocumental(models.Model):
    nome = models.CharField(max_length=20, null=True, blank=False, unique=True)

    def __str__(self):
        return self.nome

class Fase(models.Model):
    nome = models.CharField(max_length=20, null=True, blank=False, unique=True)

    def __str__(self):
        return self.nome

class Tipologia(models.Model):
    setor = models.ForeignKey(Setor, related_name='setor', null=True)
    usuario = models.ForeignKey(Usuario, related_name='usuario', null=True)
    fases = models.ManyToManyField(Fase)
    especieDocumental = models.ForeignKey(EspecieDocumental,related_name='especieDocumental', null=True)
    finalidade = models.TextField(null=True, blank=False, unique=True)
    nome = models.CharField(max_length=50, null=True, blank=False, unique=True)
    identificacao = models.CharField(max_length=50, null=True, blank=False, unique=True)
    atividade = models.ForeignKey(Atividade, related_name='atividade', null=True)
    elemento = models.ManyToManyField(Elemento, related_name='elemento')
    suporte = models.ForeignKey(Suporte, related_name='suporte', null=True)
    formaDocumental = models.ForeignKey(FormaDocumental, related_name='formaDocumental', null=True)
    genero = models.ManyToManyField(Genero, related_name='genero')
    anexo = models.ForeignKey(Opcao, related_name='anexo',null=True)
    relacaoInterna = models.ForeignKey(Opcao, related_name='relacaoInterna', null=True)
    relacaoExterna = models.ForeignKey(Opcao, related_name='relacaoExterna', null=True)
    inicioAcumulo = models.DateField(null=True)
    fimAcumulo = models.DateField(null=True)
    quantidadeAcumulada = models.CharField(max_length=50, null=True, blank=False, unique=True)
    embasamentoLegal = models.CharField(max_length=50, null=True, blank=False, unique=True)
    informacaoOutrosDocumentos = models.ForeignKey(Opcao, related_name='informacaoOutrosDocumentos', null=True)
    restricaoAcesso = models.ManyToManyField(RestricaoAcesso, related_name='restricaoAcesso')
    riscoPerda = models.ForeignKey(Opcao, related_name='riscoPerda', null=True)

    def __str__(self):
        return 'setor:'+self.setor+'usuário:'+self.usuario+'fase:'+self.fase+'espécie:'+\
               self.especie+'nome:'+self.nome
