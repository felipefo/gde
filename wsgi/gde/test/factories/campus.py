import factory
from app.models import Campus

class CampusFactory(factory.django.DjangoModelFactory):
	class Meta:
		model = Campus
		django_get_or_create = ('nome',)

	nome = 'campusTeste'