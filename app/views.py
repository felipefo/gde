from .models import Categoria
from django.shortcuts import render, get_object_or_404, redirect


def categoria(request):
    if request.POST:
        nome = request.POST.get('nome', None)
        Categoria.objects.create(nome=nome)
    return render(request, 'categoria.html', {})


def categorias_list(request):
    categorias = Categoria.objects.all
    return render(request, 'categorias_list.html', {'categorias': categorias})


def categoria_remove(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    categoria.delete()
    return redirect('app.views.categorias_list')


def categoria_edit(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.POST:
        nome = request.POST.get('nome', None)
        # categoria = Categoria.objects.get(id=pk)
        categoria.nome = nome
        categoria.save()
    return render(request, 'editarCategoria.html', {'categoria': categoria})
