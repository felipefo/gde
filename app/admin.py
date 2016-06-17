from django.contrib import admin
from .models import Setor
from .models import Categoria

admin.site.register(Categoria)
admin.site.register(Setor)

