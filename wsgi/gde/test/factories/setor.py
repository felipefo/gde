import factory
from app.models import Setor


class SetorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Setor
        django_get_or_create = ('nome', 'sigla', 'funcao',)


    nome = factory.Sequence(lambda n: "Setor %03d" % n)
    sigla = factory.Sequence(lambda n: "S %03d" % n)
    funcao = factory.Sequence(lambda n: "Funcao %03d" % n)