from django.forms import ModelForm, Select, TextInput
from .models import *


class FormAtividade(ModelForm):
    class Meta:
        model = Atividade
        fields = ['setor','descricao']


class FormSetor(ModelForm):
    class Meta:
        model = Setor
        fields = ['campus','nome', 'sigla', 'funcao', 'historico']
        widgets = {
            'campus': Select(attrs={'id':'campusselect'}),
             'nome': TextInput(attrs={'class':'validate'})
                   }
class FormCampus(ModelForm):
	class Meta:
		model = Campus
		fields = ['nome']