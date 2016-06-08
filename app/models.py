from __future__ import unicode_literals
from django.db import models


class Categoria(models.Model):
    nome = models.CharField(max_length=20, null=True, unique=True)

    def __str__(self):
        return self.nome


class Setor(models.Model):
    nome = models.CharField(max_length=20, null=True, unique=True)
    sigla = models.CharField(max_length=20, null=True, unique=True)
    funcao = models.CharField(max_length=250, null=True, unique=True)
    descricao = models.CharField(max_length=250, null=True, unique=True)

    def __str__(self):
        return self.nome
