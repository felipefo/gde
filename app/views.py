from django.shortcuts import render
from .models import Setor


# Create your views here.

def Setor(request):
    if request.POST:
        nome = request.POST.get('nome',None)
        sigla = request.POST.get('sigla',None)
        funcao = request.POST.get('funcao',None)
        descricao = request.POST.get('descricao',None)
        setor = Setor.objects.create(nome, sigla, funcao, descricao)
        setor.save()
    return render(request, 'cadastro_setor.html', {})
