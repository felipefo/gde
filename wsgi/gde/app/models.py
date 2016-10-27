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
    campus = models.ForeignKey(Campus, null=True)
    setor = models.ForeignKey(Setor, null=True)
