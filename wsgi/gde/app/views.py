from app.models import EspecieDocumental, Setor, Campus, Atividade, Tipologia
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.models import User
from .forms import FormAtividade, FormSetor, FormCampus, FormTipologia
from django.views.generic.list import ListView
from django.utils import timezone



@csrf_protect
def cadastroUsuario(request):
    if request.POST:
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        email = request.POST.get('email', None)
        nome = request.POST.get('firstname', None)
        sobrenome = request.POST.get('lastname', None)
        user = User.objects.create_user(username, email, password)
        user.first_name = nome
        user.last_name = sobrenome
        user.save()
        if user.is_active:
            return HttpResponseRedirect(request.POST.get('next'))

    return render(request, 'cadastroUsuario.html')


@csrf_protect
@login_required
def home(request):
    return render(request, 'home.html')


@csrf_protect
@login_required
def user_detail(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.POST:
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        email = request.POST.get('email', None)
        nome = request.POST.get('firstname', None)
        sobrenome = request.POST.get('lastname', None)
        user = User.objects.get(id=pk)
        user.username = username
        user.email = email
        if user.password != password:
            user.password = make_password(password)
        user.first_name = nome
        user.last_name = sobrenome
        user.save()
        messages.success(request, 'Os dados foram atualizados com sucesso.')
    return render(request, 'editarUsuario.html', {'user': user})


@csrf_protect
@login_required
def especieDocumental(request):
    if request.POST:
        nome = request.POST.get('nome', None)
        existeNoBanco = EspecieDocumental.objects.filter(nome=nome).exists()
        if (nome != ''):
            if (existeNoBanco == True):
                messages.add_message(request, messages.ERROR,
                                     'A Especie Documental ja existe. Por favor, tente novamente!')
            else:
                EspecieDocumental.objects.create(nome=nome)
                return HttpResponseRedirect(request.POST.get('next'))
    return render(request, 'especieDocumental.html', {})


@csrf_protect
@login_required
def especiesDocumentais_list(request):
    especiesDocumentais = EspecieDocumental.objects.all
    return render(request, 'especiesDocumentais_list.html', {'especiesDocumentais': especiesDocumentais})


@csrf_protect
@login_required
def especieDocumental_remove(request, pk):
    especieDocumental = get_object_or_404(EspecieDocumental, pk=pk)
    especieDocumental.delete()
    return redirect('app.views.especiesDocumentais_list')


@csrf_protect
@login_required
def especieDocumental_edit(request, pk):
    especieDocumental = get_object_or_404(EspecieDocumental, pk=pk)
    # if request.POST:
    #     nome = request.POST.get('nome', None)
    #     especieDocumental.nome = nome
    #     especieDocumental.save()
    #     return HttpResponseRedirect(request.POST.get('next'))

    if request.POST:
        nome = request.POST.get('nome', None)
        existeNoBanco = EspecieDocumental.objects.filter(nome=nome).exists()
        if (nome != ''):
            if (existeNoBanco == True):
                messages.add_message(request, messages.ERROR,
                                     'A Especie Documental ja existe. Por favor, tente novamente!')
            else:
                nome = request.POST.get('nome', None)
                especieDocumental.nome = nome
                especieDocumental.save()
                return HttpResponseRedirect(request.POST.get('next'))

    return render(request, 'editarEspecieDocumental.html', {'especieDocumental': especieDocumental})

@csrf_protect
@login_required
def atividades_list(request):
    atividades = Atividade.objects.order_by('setor')
    return render(request, 'atividades_list.html', {'atividades': atividades})

@csrf_protect
@login_required()
def atividade(request):
    if request.method == 'POST':
        form = FormAtividade(request.POST)
        if form.is_valid():
            setor = form.cleaned_data['setor']
            descricao = form.cleaned_data['descricao']
            Atividade.objects.create(setor=setor,descricao=descricao)
            return HttpResponseRedirect('/atividades_list/')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = FormAtividade()

    return render(request, 'atividade.html', {'form': form})

@csrf_protect
@login_required
def atividade_edit(request, pk):
    atividade = get_object_or_404(Atividade, pk=pk)
    if request.POST:
        form = FormAtividade(request.POST, instance=atividade)
        if form.is_valid():
            atividade = form.save(commit=False)
            atividade.setor = form.cleaned_data['setor']
            atividade.descricao = form.cleaned_data['descricao']
            atividade.save()
            return HttpResponseRedirect(request.POST.get('next'))
    else:
        form = FormAtividade(instance=atividade)
    return render(request, 'editar_atividade.html', {'form': form, 'atividade': atividade})

@csrf_protect
@login_required
def atividade_remove(request, pk):
    atividade = get_object_or_404(Atividade, pk=pk)
    atividade.delete()
    return redirect('app.views.atividades_list')

@csrf_protect
@login_required
def setores_list(request):
    setores = Setor.objects.all
    return render(request, 'setores_list.html', {'setores': setores})


@csrf_protect
@login_required()
def cadastrar_setor(request):
    if request.method == 'POST':
        form = FormSetor(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            sigla = form.cleaned_data['sigla']
            funcao = form.cleaned_data['funcao']
            historico = form.cleaned_data['historico']
            Setor.objects.create(nome=nome, sigla=sigla, funcao=funcao, historico=historico)
            return HttpResponseRedirect(request.POST.get('next'))
    else:
        form = FormSetor()

    return render(request, 'cadastro_setor.html', {'form': form})


@csrf_protect
@login_required
def setor_edit(request, pk):
    setor = get_object_or_404(Setor, pk=pk)
    if request.POST:
        form = FormSetor(request.POST, instance=setor)
        if form.is_valid():
            setor = form.save(commit=False)
            setor.campus = form.cleaned_data['campus']
            setor.nome = form.cleaned_data['nome']
            setor.sigla = form.cleaned_data['sigla']
            setor.funcao = form.cleaned_data['funcao']
            setor.historico = form.cleaned_data['historico']
            setor.save()
            return HttpResponseRedirect(request.POST.get('next'))
    else:
        form = FormSetor(instance=setor)
    return render(request, 'editar_setor.html', {'form': form, 'setor': setor})


@csrf_protect
@login_required
def setor_remove(request, pk):
    setor = get_object_or_404(Setor, pk=pk)
    setor.delete()
    return redirect('app.views.setores_list')


@csrf_protect
@login_required
def campus(request):
    if request.method == 'POST':
        form = FormCampus(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            Campus.objects.create(nome=nome)
            return HttpResponseRedirect(request.POST.get('next'))
    else:
        form = FormCampus()
    return render(request, 'campus.html', {'form': form})


@csrf_protect
@login_required
def campi_list(request):
    campi = Campus.objects.all
    return render(request, 'campi_list.html', {'campi': campi})


@csrf_protect
@login_required
def campus_edit(request, pk):
    campus = get_object_or_404(Campus, pk=pk)
    if request.POST:
        form = FormCampus(request.POST, instance=campus)
        if form.is_valid():
            campus = form.save(commit=False)
            if(Campus.objects.filter(nome=form.cleaned_data['nome'])):
                form.add_error('nome', 'Campus com este Nome já existe.')
            else:
                campus.nome = form.cleaned_data['nome']
                campus.save()
                return HttpResponseRedirect(request.POST.get('next'))
    else:
        form = FormCampus(instance=campus)
    return render(request, 'editarCampus.html', {'form': form, 'campus': campus})

@csrf_protect
@login_required
def campus_remove(request, pk):
    campus = get_object_or_404(Campus, pk=pk)
    campus.delete()
    return redirect('app.views.campi_list')

@csrf_protect
@login_required()
def cadastrar_tipologia(request):
    if request.method == 'POST':
        form = FormTipologia(request.POST)
        if form.is_valid():
            setor = form.cleaned_data['setor']
            usuario = form.cleaned_data['usuario']
            fase = form.cleaned_data['fase']
            especieDocumental = form.cleaned_data['especieDocumental']
            finalidade = form.cleaned_data['finalidade']
            nome = form.cleaned_data['nome']
            identificacao = form.cleaned_data['identificacao']
            atividade = form.cleaned_data['atividade']
            elemento = form.cleaned_data['elemento']
            suporte = form.cleaned_data['suporte']
            formaDocumental = form.cleaned_data['formaDocumental']
            genero = form.cleaned_data['genero']
            anexo = form.cleaned_data['anexo']
            relacaoInterna = form.cleaned_data['relacaoInterna']
            relacaoExterna = form.cleaned_data['relacaoExterna']
            inicioAcumulo = form.cleaned_data['inicioAcumulo']
            fimAcumulo = form.cleaned_data['fimAcumulo']
            quantidadeAcumulada = form.cleaned_data['quantidadeAcumulada']
            embasamentoLegal = form.cleaned_data['embasamentoLegal']
            informacaoOutrosDocumentos = form.cleaned_data['informacaoOutrosDocumentos']
            restricaoAcesso = form.cleaned_data['restricaoAcesso']
            riscoPerda = form.cleaned_data['riscoPerda']
            sugestao = form.cleaned_data['sugestao']
            Tipologia.objects.create(setor = setor, usuario = usuario, fase = fase, especieDocumental = especieDocumental, finalidade = finalidade, nome = nome, identificacao = identificacao, atividade = atividade, elemento = elemento, suporte = suporte, formaDocumental = formaDocumental, genero = genero, anexo = anexo, relacaoInterna = relacaoInterna, relacaoExterna = relacaoExterna, inicioAcumulo = inicioAcumulo, fimAcumulo = fimAcumulo, quantidadeAcumulada = quantidadeAcumulada, embasamentoLegal = embasamentoLegal, informacaoOutrosDocumentos = informacaoOutrosDocumentos, restricaoAcesso = restricaoAcesso, riscoPerda = riscoPerda, sugestao = sugestao)
            return HttpResponseRedirect(request.POST.get('next'))
    else:
        form = FormTipologia()

    return render(request, 'cadastro_tipologia.html', {'form': form})
