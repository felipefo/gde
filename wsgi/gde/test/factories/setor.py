import factory
from app.models import Setor


class SetorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Setor
        django_get_or_create = ('nome', 'sigla', 'funcao',)


nome = 'setorTeste'
sigla = 'siglaTeste'
funcao = 'funcaoTeste'