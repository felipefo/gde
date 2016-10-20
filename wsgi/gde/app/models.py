from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models


class EspecieDocumental(models.Model):
    nome = models.CharField(max_length=20, null=True, blank=False, unique=True)

    def __str__(self):
        return self.nome


class Atividade(models.Model):
    descricao = models.TextField(null=True, blank=False, unique=True)

    def __str__(self):
        return self.descricao


class Historico(models.Model):
    nome = models.CharField(max_length=20, null=True, blank=False, unique=True)

    def __str__(self):
        return self.nome


class Setor(models.Model):
    nome = models.CharField(max_length=20, null=True, blank=False, unique=True)
    sigla = models.CharField(max_length=20, null=True, blank=False, unique=True)
    funcao = models.CharField(max_length=250, null=True, blank=False, unique=True)
    atividade = models.ForeignKey(Atividade, null=True)
    historico = models.ForeignKey(Historico, null=True)

    def __str__(self):
        return self.nome


class Campus(models.Model):
    nome = models.CharField(max_length=30, null=True, blank=False, unique=True)
    setores = models.ManyToManyField(Setor)

    def __str__(self):
        return self.nome


class CampusSetor(models.Model):
    campus = models.ForeignKey(Campus)
    setor = models.ForeignKey(Setor)


class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    lotacao = models.ForeignKey(CampusSetor, null=True)
