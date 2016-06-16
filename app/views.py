from .models import Categoria
from django.shortcuts import render


def categoria(request):
    if request.POST:
        nome = request.POST.get('nome', None)
        Categoria.objects.create(nome=nome)
    return render(request, 'categoria.html', {})

def categorias_list(request):
    categorias = Categoria.objects.all
    return render(request, 'categorias_list.html', {'categorias': categorias})

