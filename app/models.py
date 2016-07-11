from __future__ import unicode_literals

from _ast import Not

from django.contrib.auth.models import User
from django.db import models


class Categoria(models.Model):
    nome = models.CharField(max_length=20, null=False, unique=True)

    def __str__(self):
        return self.nome

class Setor(models.Model):
    nome = models.CharField(max_length=20, null=False, unique=True)
    sigla = models.CharField(max_length=20, null=False, unique=True)
    funcao = models.CharField(max_length=250, null=False, unique=True)


    def __str__(self):
        nome = models.CharField(max_length=20, null=False, unique=True)
        return self.nome


class Usuario(models.Model):
    user = models.ForeignKey(User)
