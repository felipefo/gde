from django.contrib import admin
from .models import Setor
from .models import EspecieDocumental,Campus,Atividade, Tipologia

admin.site.register(Campus)
admin.site.register(Atividade)
admin.site.register(EspecieDocumental)
admin.site.register(Setor)
admin.site.register(Tipologia)

