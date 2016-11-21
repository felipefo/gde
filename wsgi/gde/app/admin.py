from django.contrib import admin
from .models import *
from .models import Setor, EspecieDocumental,Campus,Atividade, Tipologia

admin.site.register(Campus)
admin.site.register(Atividade)
admin.site.register(EspecieDocumental)
admin.site.register(Setor)
admin.site.register(Tipologia)
admin.site.register(Elemento)
admin.site.register(Suporte)
admin.site.register(Genero)
admin.site.register(RestricaoAcesso)
admin.site.register(FormaDocumental)
admin.site.register(Fase)






