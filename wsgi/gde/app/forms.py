from django.forms import ModelForm
from .models import *


class FormAtividade(ModelForm):
    class Meta:
        model = Atividade
        fields = ['setor','descricao']


class FormSetor(ModelForm):
    class Meta:
        model = Setor
        fields = ['campus','nome', 'sigla', 'funcao', 'historico']
