from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
import datetime

def gera_anos(anoInicial):
    YEAR_CHOICES = []
    for r in range(anoInicial, (datetime.datetime.now().year+1)):
        YEAR_CHOICES.append((r,r))
    return YEAR_CHOICES

def gera_inteiros_positivos(quantidade):
    inteiros_positivos = []
    for r in range(quantidade):
        inteiros_positivos.append((r, r))
    return inteiros_positivos

def gera_sim_nao():
    saida = [(True, 'Sim'), (False, 'Não')]
    return saida

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

opcoes = ((True, 'Produzido neste setor'), (False, 'Recebido por este setor'))

class TipoAcumulo(models.Model):
    nome = models.CharField(max_length=30, null=True, blank=False, unique=False)
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
    anexo = models.BooleanField(choices=gera_sim_nao(), default=True)
    relacaoInterna = models.BooleanField(choices=gera_sim_nao(), default=True)
    relacaoExterna = models.BooleanField(choices=gera_sim_nao(), default=True)
    inicioAcumulo = models.IntegerField(choices=gera_anos(1900), default=1970)
    quantidadeVias = models.BooleanField(choices=gera_sim_nao(), default=True)
    fimAcumulo = models.IntegerField(choices=gera_anos(1900), default=datetime.datetime.now().year)
    quantidadeAcumulada = models.IntegerField(choices=gera_inteiros_positivos(100), default=0)
    tipoAcumulo = models.ManyToManyField(TipoAcumulo, related_name='tipoAcumulo')
    embasamentoLegal = models.CharField(max_length=50, null=True, blank=False, unique=True)
    informacaoOutrosDocumentos = models.BooleanField(choices=gera_sim_nao(), default=True)
    restricaoAcesso = models.ManyToManyField(RestricaoAcesso, related_name='restricaoAcesso')
    riscoPerda = models.BooleanField(choices=gera_sim_nao(), default=True)
    producaoSetor = models.BooleanField(choices=opcoes, default=True)

    def __str__(self):
        return 'setor:'+self.setor.nome+'usuário:'+self.usuario.user.username+'espécie:'+\
               self.especieDocumental.nome+'nome:'+self.nome
