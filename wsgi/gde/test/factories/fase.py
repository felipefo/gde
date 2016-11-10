import factory
from app.models import Fase

class FaseFactory(factory.django.DjangoModelFactory):
	class Meta:
		model = Fase
		django_get_or_create = ('nome',)

	nome = factory.Sequence(lambda n: "Fase %03d" % n)