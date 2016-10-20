from django import forms

class FormAtividade(forms.Form):
    descricao = forms.CharField(label='Descrição da atividade', widget=forms.Textarea, required=True)