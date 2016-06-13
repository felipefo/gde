from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.models import User


@csrf_protect
def cadastroUsuario(request):
    if request.POST:
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        email = request.POST.get('email', None)
        user = User.objects.create_user(username,  email, password)
    if user.is_active:
        return HttpResponseRedirect(request.POST.get('next'))

    return render(request, 'cadastroUsuario.html')

@csrf_protect
def home(request):
    return render(request, 'home.html')