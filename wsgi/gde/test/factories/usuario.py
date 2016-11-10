import factory
from app.models import Usuario
from test.factories.user import UserFactory
from test.factories.setor import SetorFactory

class UsuarioFactory(factory.django.DjangoModelFactory):
	class Meta:
		model = Usuario

	user = factory.SubFactory(UserFactory)
	setor = factory.SubFactory(SetorFactory)
