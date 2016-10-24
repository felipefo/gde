from django.forms import ModelForm
from .models import *


class FormAtividade(ModelForm):
    class Meta:
        model = Atividade
        fields = ['descricao']


class FormSetor(ModelForm):
    class Meta:
        model = Setor
        fields = ['campus','nome', 'sigla', 'funcao', 'atividade', 'historico']
