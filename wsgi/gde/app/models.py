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
    campus = models.ForeignKey(Campus, null=True, blank=False, verbose_name='Campus')
    nome = models.CharField(max_length=20, null=True, blank=False, unique=False)
    sigla = models.CharField(max_length=20, null=True, blank=False, unique=False)
    funcao = models.CharField(max_length=250, null=True, blank=False, unique=False)
    historico = models.CharField(max_length=250, null=True, blank=True, unique=False)

    def __str__(self):
        return self.nome

class Atividade(models.Model):
    setor = models.ForeignKey(Setor, null=True, blank=False)
    descricao = models.TextField(null=True, blank=False, unique=True)

    def __str__(self):
        return self.descricao

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    setor = models.ForeignKey(Setor, null=True, blank=False, verbose_name='Setor')

    def __str__(self):
        return self.user.first_name

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
    anexo = models.ManyToManyField(Opcao, related_name='anexo')
    relacaoInterna = models.ManyToManyField(Opcao, related_name='relacaoInterna')
    relacaoExterna = models.ManyToManyField(Opcao, related_name='relacaoExterna')
    inicioAcumulo = models.DateField(null=True)
    fimAcumulo = models.DateField(null=True)
    quantidadeAcumulada = models.CharField(max_length=50, null=True, blank=False, unique=True)
    embasamentoLegal = models.CharField(max_length=50, null=True, blank=False, unique=True)
    informacaoOutrosDocumentos = models.ManyToManyField(Opcao, related_name='informacaoOutrosDocumentos')
    restricaoAcesso = models.ManyToManyField(RestricaoAcesso, related_name='restricaoAcesso')
    riscoPerda = models.ManyToManyField(Opcao, related_name='riscoPerda')
    sugestao = models.TextField(null=True, blank=False, unique=True)


    def __str__(self):
        return 'setor:'+self.setor.nome+'usuário:'+self.usuario.user.username+'espécie:'+\
               self.especieDocumental.nome+'nome:'+self.nome
