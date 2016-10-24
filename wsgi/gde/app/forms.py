from django.forms import ModelForm
from .models import *


class FormAtividade(ModelForm):
    class Meta:
        model = Atividade
        fields = ['descricao']


class FormSetor(ModelForm):
    class Meta:
        model = Setor
        fields = ['nome', 'sigla', 'funcao', 'atividade', 'historico']
