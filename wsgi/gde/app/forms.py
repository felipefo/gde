from django import forms
from django.forms import ModelForm, Select, TextInput, EmailInput, ChoiceField, CharField, EmailInput,RadioSelect, ModelMultipleChoiceField, SelectMultiple
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
    def __init__(self, *args, **kwargs):
        setor = kwargs.pop('setor', None)
        super(FormTipologia, self).__init__(*args,**kwargs)
        self.fields['atividade'] = forms.ModelChoiceField(required=False, queryset=Atividade.objects.filter(setor=setor), widget=forms.Select())
        for field in self.fields:
            help_text = self.fields[field].help_text
            self.fields[field].help_text = None
            if help_text != '':
                self.fields[field].widget.attrs.update({'class':'tooltipped', 'data-tooltip':help_text, 'data-position':'top', 'data-delay':50})

    class Meta:
        model = Tipologia

        fields = ['producaoSetor', 'especieDocumental', 'finalidade', 'nome', 'identificacao', 'atividade',
                  'elemento', 'suporte', 'formaDocumental','quantidadeVias', 'genero', 'anexo', 'relacaoInterna', 'relacaoExterna',
                  'inicioAcumulo', 'fimAcumulo','quantidadeAcumulada','tipoAcumulo', 'embasamentoLegal',
                  'informacaoOutrosDocumentos', 'restricaoAcesso']
        widgets = {
            'suporte': Select(attrs={'class':'browser-default'})
        }

        labels = {
            'producaoSetor':'Este documento é',
            'especieDocumental':'Espécie documental',
            'identificacao':'Identificações no documento',
            'atividade':'Atividade relacionada ao documento',
            'formaDocumental':'Forma documental',
            'elementos':'Elementos apresentados',
            'genero':'Gênero documental',
            'nome':'Nome do documento',
            'finalidade':'Ação/Finalidade',
            'relacaoInterna':'Relação interna',
            'relacaoExterna':'Relação externa',
            'inicioAcumulo':'Período acumulado',
            'fimAcumulo':'',
            'quantidadeAcumulada':'Quantidade acumulada',
            'quantidadeVias':'Quantidade de vias',
            'tipoAcumulo':'',
            'embasamentoLegal':'Embasamento Legal',
            'informacaoOutrosDocumentos':'Informações registradas em outros documentos',
            'restricaoAcesso':'Restrição de acesso',
        }
        help_texts={
            'finalidade':'Dica: Ação que gerou este documento / Objetivo para o qual foi produzido',
            'nome':'Dica: Nome utilizado pelo setor para identificar o documento (Ex.: Folha de Ponto; Relatório de Atividades).',
            'identificacao':'Dica: Números e siglas presentes no documento (Ex.: Mem. nº 006-2016-DACV)',
            'atividade':'Dica: Este documento está relacionado a qual atividade do setor?',
            'elemento':'Dica: Marque os itens presentes neste documento',
            'suporte':'Dica: Em qual suporte a informação circula?',
            'formaDocumental':'Forma documental',
            'genero':'Dica: Qual o gênero predominante do documento?',
            'relacaoInterna':'Dica: Este documento será encaminhado para outros setores?',
            'anexo':'Dica: Este documento pussui anexo?',
            'relacaoExterna':'Dica: Este documento será encaminhado para algum órgão externo ao Ifes?',
            'inicioAcumulo':'Dica: Qual o período de abrangência deste tipo de documento?',
            'quantidadeAcumulada':'Dica: Qual a quantidade e a forma de armazenamento deste documento?',
            'quantidadeVias':'Dica: Produz mais de uma via deste documento? ',
            'embasamentoLegal':'Dica: Existe alguma normativa ou legislação específica sobre a configuração (Boletim, certidão, etc) que este documento possui e o conteúdo tratado nele?',
            'informacaoOutrosDocumentos':'Dica: As informações que estão neste documento encontram-se também em outros? (Ex: relatórios parciais que têm suas informações compiladas em um relatório final)',
            'restricaoAcesso':'Dica: O documento contém informações que necessitam de restrição de acesso?',
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
