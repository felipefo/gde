from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.models import User


@csrf_protect
def cadastroUsuario(request):
    # username = request.POST.get('username', False)
    # password = request.POST.get('password', False)
    # user = User.objects.create_user(username, password)
    return render(request, 'cadastroUsuario.html', {})
