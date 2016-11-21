import factory
from app.models import Tipologia


class TipologiaFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Tipologia
        django_get_or_create = ('setor', 'usuario', 'fase', 'especieDocumental', 'finalidade', 'nome', 'identificacao', 'atividade', 'elemento', 'suporte', 'formaDocumental', 'genero', 'anexo', 'relacaoInterna', 'relacaoExterna', 'inicioAcumulo', 'fimAcumulo', 'quantidadeAcumulada', 'embasamentoLegal', 'informacaoOutrosDocumentos', 'restricaoAcesso', 'riscoPerda', 'sugestao')

setor = 'setorTeste'
usuario = 'usuarioTeste'
fase = 'faseTeste'
especieDocumental = 'especieDocumentalTeste'
finalidade = 'finalidadeTeste'
nome = 'nomeTeste'
identificacao = 'identificacaoTeste'
atividade = 'atividadeTeste'
elemento = 'elementoTeste'
suporte = 'suporteTeste'
formaDocumental = 'formaDocumentalTeste'
genero = 'generoTeste'
anexo = 'anexoTeste'
relacaoInterna = 'relacaoInternaTeste'
relacaoExterna = 'relacaoExternaTeste'
inicioAcumulo = 'inicioAcumuloTeste'
fimAcumulo = 'fimAcumuloTeste'
quantidadeAcumulada = 'quantidadeAcumuladaTeste'
embasamentoLegal = 'embasamentoLegalTeste'
informacaoOutrosDocumentos = 'informacaoOutrosDocumentosTeste'
restricaoAcesso = 'restricaoAcessoTeste'
riscoPerda = 'riscoPerdaTeste'
sugestao = 'sugestaoTste'