from django.contrib import admin
from .models import Setor
from .models import EspecieDocumental, Campus, Atividade,Elemento, Suporte, Genero, RestricaoAcesso, Fase, Tipologia, Usuario, TipoAcumulo, Conarq, Resposta, GrupoConarq

admin.site.register(Campus)
admin.site.register(Atividade)
admin.site.register(EspecieDocumental)
admin.site.register(Setor)
admin.site.register(TipoAcumulo)
admin.site.register(Elemento)
admin.site.register(Suporte)
admin.site.register(Genero)
admin.site.register(RestricaoAcesso)
admin.site.register(Fase)
admin.site.register(Tipologia)
admin.site.register(Usuario)

admin.site.register(GrupoConarq)
admin.site.register(Conarq)
admin.site.register(Resposta)