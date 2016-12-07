from behave import given, when, then
from test.factories.tipologia import TipologiaFactory
from test.factories.fase import FaseFactory
from app.models import Tipologia, Campus
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from test.factories.campus import CampusFactory


# @when('Clico na opcao Meus Levantamentos')
# def step_impl(context):
#     br = context.browser
#     br.get(context.base_url + '/home')
#     br.get_screenshot_as_file('/tmp/screenshot.png')
#     fase = FaseFactory(nome='Levantamento')
#     tipologia = TipologiaFactory()
#     assert tipologia.nome == 'Nome da Tipologia 000'
#
#     br.find_element_by_id('id-meus-levantamentos').click()

@then('sou redirecionado para a pagina com a lista de levantamentos feitos pelo usuario')
def step_impl(context):
    pass

@then('Devem ser listados todos os levantamentos já cadastrados no sistema.')
def step_impl(context):
    pass




# Scenario: Cadastrar nova tipologia
@given('Estou na pagina de cadastro de uma tipologia')
def step_impl(context):
    br = context.browser
    br.get(context.base_url + '/tipologia')

    # Checks for Cross-Site Request Forgery protection input
    assert br.find_element_by_name('csrfmiddlewaretoken').is_enabled()
    assert br.current_url.endswith('/tipologia/')


@when('Clico na opcao Meus Levantamentos')
def step_impl(context):
    pass


@when('Informo os dados do formulario')
def step_impl(context):
    pass
    # br = context.browser
    #
    # campus = CampusFactory(nome='Serra')
    # campus.save()
    # campus = Campus.objects.filter(nome='Serra').exists()
    # assert campus == True
    #
    # #br.get_screenshot_as_file('/tmp/screenshot.png')
    #
    # br.find_element_by_name('setor').send_keys('setorTeste')
    # br.find_element_by_name('usuario').send_keys('usuarioTeste')
    # br.find_element_by_name('fase').send_keys('faseTeste')
    # br.find_element_by_name('especieDocumental').send_keys('especieDocumentalTeste')
    # br.find_element_by_name('finalidade').send_keys('finalidadeTeste')
    # br.find_element_by_name('identificacao').send_keys('identificacaoTeste')
    # br.find_element_by_name('nome').send_keys('nomeTeste')
    # br.find_element_by_name('atividade').send_keys('atividadeTeste')
    # br.find_element_by_name('elemento').send_keys('elementoTeste')
    # br.find_element_by_name('suporte').send_keys('suporteTeste')
    # br.find_element_by_name('formaDocumental').send_keys('formaDocumentalTeste')
    # br.find_element_by_name('genero').send_keys('generoTeste')
    # br.find_element_by_name('anexo').send_keys('anexoTeste')
    # br.find_element_by_name('relacaoInterna').send_keys('relacaoInternaTeste')
    # br.find_element_by_name('relacaoExterna').send_keys('relacaoExternaTeste')
    # br.find_element_by_name('inicioAcumulo').send_keys('inicioAcumuloTeste')
    # br.find_element_by_name('fimAcumulo').send_keys('fimAcumuloTeste')
    # br.find_element_by_name('quantidadeAcumulada').send_keys('quantidadeAcumuladaTeste')
    # br.find_element_by_name('embasamentoLegal').send_keys('embasamentoLegalTeste')
    # br.find_element_by_name('informacaoOutrosDocumentos').send_keys('informacaoOutrosDocumentosTeste')
    # br.find_element_by_name('restricaoAcesso').send_keys('restricaoAcessoTeste')
    # br.find_element_by_name('riscoPerda').send_keys('riscoPerdaTeste')
    # br.find_element_by_name('sugestao').send_keys('sugestaoTeste')
    # br.find_element_by_name('submit').click()
    #
    # assert br.find_element_by_name('csrfmiddlewaretoken').is_enabled()


@when('Nao existir uma tipologia com os mesmos dados ja cadastrado')
def step_impl(context):
    pass


@when('Submeto o cadastro de um nova tipologia')
def step_impl(context):
    pass
    # br = context.browser
    #
    # # Checks for Cross-Site Request Forgery protection input
    # assert br.find_element_by_name('csrfmiddlewaretoken').is_enabled()
    #
    # # Fill login form and submit it (valid version)
    # br.find_element_by_name('submit').click()


@then('Sou redirecionado para a pagina principal do sistema')
def step_impl(context):
    pass
    # br = context.browser
    # # br.get_screenshot_as_file('/tmp/screenshot.png')
    # # Checks success status
    # assert br.current_url.endswith('/home/')
    # assert br.find_element_by_name('nome').text == ""


@then('A tipologia devera estar devidamente cadastrado.')
def step_impl(context):
    pass
    # br = context.browser
    # assert br.current_url.endswith('/setor/')
    # assert br.find_element_by_name('nome').text == ""


@when('Informo uma tipologia ja cadastrado no sistema')
def step_impl(context):
    pass
    #
    # br = context.browser
    #
    # br.find_element_by_name('setor ').send_keys('setorTeste')
    # br.find_element_by_name('usuario ').send_keys('usuarioTeste')
    # br.find_element_by_name('fase ').send_keys('faseTeste')
    # br.find_element_by_name('especieDocumental ').send_keys('especieDocumentalTeste')
    # br.find_element_by_name('finalidade ').send_keys('finalidadeTeste')
    # br.find_element_by_name('identificacao ').send_keys('identificacaoTeste')
    # br.find_element_by_name('nome ').send_keys('nomeTeste')
    # br.find_element_by_name('atividade ').send_keys('atividadeTeste')
    # br.find_element_by_name('elemento ').send_keys('elementoTeste')
    # br.find_element_by_name('suporte ').send_keys('suporteTeste')
    # br.find_element_by_name('formaDocumental ').send_keys('formaDocumentalTeste')
    # br.find_element_by_name('genero ').send_keys('generoTeste')
    # br.find_element_by_name('anexo ').send_keys('anexoTeste')
    # br.find_element_by_name('relacaoInterna ').send_keys('relacaoInternaTeste')
    # br.find_element_by_name('relacaoExterna ').send_keys('relacaoExternaTeste')
    # br.find_element_by_name('inicioAcumulo ').send_keys('inicioAcumuloTeste')
    # br.find_element_by_name('fimAcumulo ').send_keys('fimAcumuloTeste')
    # br.find_element_by_name('quantidadeAcumulada ').send_keys('quantidadeAcumuladaTeste')
    # br.find_element_by_name('embasamentoLegal ').send_keys('embasamentoLegalTeste')
    # br.find_element_by_name('informacaoOutrosDocumentos ').send_keys('informacaoOutrosDocumentosTeste')
    # br.find_element_by_name('restricaoAcesso ').send_keys('restricaoAcessoTeste')
    # br.find_element_by_name('riscoPerda ').send_keys('riscoPerdaTeste')
    # br.find_element_by_name('sugestao ').send_keys('sugestaoTeste')
    # br.find_element_by_name('submit').click()
    #
    # tipologia = Tipologia.objects.filter(nome = 'setorTeste', sigla = 'ST').exists()
    # # br.get_screenshot_as_file('/tmp/screenshot.png')
    # assert tipologia == True
    # assert br.find_element_by_name('csrfmiddlewaretoken').is_enabled()
    # assert br.current_url.endswith('/tipologia/')



@then('Recebo uma mensagem de erro informando que a tipologia ja existe.')
def step_impl(context):
    pass


@then('Nao conseguirei cadastrar a tipologia ate que eu preencha com dados diferentes.')
def step_impl(context):
    pass

@when('Submeto o cadastro de uma nova tipologia')
def step_impl(context):
    pass






