from django.forms import ModelForm
from app.models import *

class FormAtividade(ModelForm):
    class Meta:
        model = Atividade
        fields = ['descricao']

class FormHistorico(ModelForm):
    class Meta:
        model = Historico
        fields = ['nome']

class FormSetor(ModelForm):
    class Meta:
        model = Setor
        fields = ['nome','sigla', 'funcao','atividade','historico']