from django import forms
from django.forms import ModelForm, Select, TextInput, EmailInput, ChoiceField, CharField, EmailInput
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

        fields = ['setor', 'usuario', 'fases', 'especieDocumental', 'finalidade', 'nome', 'identificacao', 'atividade',
                  'elemento', 'suporte', 'formaDocumental', 'genero', 'anexo', 'relacaoInterna', 'relacaoExterna',
                  'inicioAcumulo', 'fimAcumulo', 'quantidadeAcumulada', 'embasamentoLegal',
                  'informacaoOutrosDocumentos', 'restricaoAcesso', 'riscoPerda','sugestao']
        widgets = {
            'inicioAcumulo': TextInput(attrs={'type': 'date', 'class': 'datepicker'}),
            'fimAcumulo': TextInput(attrs={'class': 'datepicker'})
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
