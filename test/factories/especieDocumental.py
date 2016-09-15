import factory
from app.models import Categoria

class CategoriaFactory(factory.django.DjangoModelFactory):
	class Meta:
		model = Categoria
		django_get_or_create = ('nome')
	nome = 'categoriaTeste'
