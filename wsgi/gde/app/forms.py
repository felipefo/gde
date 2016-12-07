from django import forms
from django.forms import ModelForm, Select, TextInput, EmailInput, ChoiceField, CharField, EmailInput,RadioSelect
from .models import *
from django.contrib.auth.models import User


class FormAtividade(ModelForm):
    class Meta:
        model = Atividade
        fields = ['setor', 'descricao']


class FormSetor(ModelForm):
    class Meta:
        model = Setor
        fields = ['campus', 'nome', 'sigla', 'funcao', 'historico']
        widgets = {
            'campus': Select(attrs={'id':'id-campus','class':'browser-default selectField'}),
             'nome': TextInput(attrs={'class':'validate'})
                    }
class FormCampus(ModelForm):
    class Meta:
        model = Campus
        fields = ['nome']


class FormTipologia(ModelForm):
    class Meta:
        model = Tipologia

        fields = ['especieDocumental', 'finalidade', 'nome', 'identificacao', 'atividade',
                  'elemento', 'suporte', 'formaDocumental', 'genero', 'anexo', 'relacaoInterna', 'relacaoExterna',
                  'inicioAcumulo', 'fimAcumulo', 'quantidadeAcumulada','tipoAcumulo', 'embasamentoLegal',
                  'informacaoOutrosDocumentos', 'restricaoAcesso', 'riscoPerda', 'producaoSetor']
        widgets = {
            'tipoAcumulo': Select()
        }

        labels = {
            'producaoSetor':'Este documento é',
            'especieDocumental':'Espécie documental',
            'identificacao':'Identificação',
            'formaDocumental':'Forma documental',
            'genero':'Gênero',
            'relacaoInterna':'Relação interna',
            'relacaoExterna':'Relação externa',
            'inicioAcumulo':'Período acumulado',
            'fimAcumulo':'',
            'quantidadeAcumulada':'Quantidade acumulada',
            'tipoAcumulo':'',
            'embasamentoLegal':'Embasamento Legal',
            'informacaoOutrosDocumentos':'Informações registradas em outros documentos',
            'restriscaoAcesso':'Restrição de acesso',
            'riscoPerda':'Risco de perda',
        }

class FormUser(ModelForm):
    first_name = forms.CharField(label='Nome', max_length=30)
    last_name = forms.CharField(label='Sobrenome', max_length=30)
    email = forms.EmailField(label='Email')

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']
        widgets = {
            'username': TextInput(attrs={'id':'id-username'}),
            'password':TextInput(attrs={'id':'id-password', 'type':'password'}),

        }
        labels = {
            'username': ('SIAPE:'),
            'password': ('Senha:'),

        }
        help_texts={
            'username':'',
        }

class FormParcialSetor(ModelForm):
    class Meta:
        model = Setor
        exclude = ['nome', 'sigla', 'funcao', 'historico']
        widgets = {
            'campus': Select(attrs={'id':'id-campus','class':'browser-default selectField'})
                    }


class FormUsuario(ModelForm):
    class Meta:
        model = Usuario
        fields = ['setor']
        widgets = {
            'setor': Select(attrs={'id':'id-setor','class':'browser-default selectField'}),
        }
