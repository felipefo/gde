from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.models import User


@csrf_protect
def cadastroUsuario(request):
    if request.POST:
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        email = request.POST.get('email', None)
        user = User.objects.create_user(username, email, password)
        if user.is_active:
            return HttpResponseRedirect(request.POST.get('next'))

    return render(request, 'cadastroUsuario.html')


@csrf_protect
@login_required
def home(request):
    return render(request, 'home.html')


def user_detail(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.POST:
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        email = request.POST.get('email', None)
        user = User.objects.get(id=pk)
        user.username = username
        user.email = email
        user.password = make_password(password)
        user.save()
    return render(request, 'editarUsuario.html', {'user': user})

