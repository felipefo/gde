from behave import given, when, then
from app.models import Campus


@given('que eu estou na pagina de cadastrar campus')
def step_impl(context):
    br = context.browser
    br.get(context.base_url + '/campus')

    # Checks for Cross-Site Request Forgery protection input
    assert br.find_element_by_name('csrfmiddlewaretoken').is_enabled()
    assert br.current_url.endswith('/campus/')

@given('Informo um nome ainda nao cadastrado no sistema')
def step_impl(context):

    br = context.browser

    # Checks for Cross-Site Request Forgery protection input
    assert br.find_element_by_name('csrfmiddlewaretoken').is_enabled()

    # Fill login form and submit it (valid version)
    campus = Campus.objects.filter(nome='Vitória').exists()
    assert campus == False
    br.find_element_by_name('nome').send_keys('Vitória')
    assert br.find_element_by_id('nome').get_attribute('value') == 'Vitória'

@when('clico no botão enviar')
def step_impl(context):
        br = context.browser
        assert br.find_element_by_name('csrfmiddlewaretoken').is_enabled()
        br.find_element_by_name('submit').click()

@then('sou redirecionado para a pagina com a lista de campi cadastrados')
def step_impl(context):
    br = context.browser

    # Checks success status
    assert br.current_url.endswith('/campi_list/')

@then('o campus deve estar devidamento cadastrado')
def step_impl(context):
    br = context.browser

    # Checks success status
    assert br.current_url.endswith('/campi_list/')
    assert br.find_element_by_id('nomeCampus').text == "Vitória"

@given('preencho o nome do campus em branco')
def step_impl(context):
        br = context.browser
        br.find_element_by_id('nome').clear()
        assert br.find_element_by_id('nome').get_attribute('value') == ""

@then('nao conseguirei cadastrar o campus ate que eu preencha o campo nome')
def step_impl(context):
    br = context.browser
    # Checks success status
    assert br.current_url.endswith('/campus/')
    assert br.find_element_by_id('nome').text == ""

@given('informo um nome ja cadastrado no sistema')
def step_impl(context):
    br = context.browser
    br.get(context.base_url + '/campus')
    especie = Campus.objects.filter(nome='Vitória').exists()
    br.find_element_by_id('nome').send_keys('Vitória')
    assert  especie == True
    assert br.find_element_by_id('nome').get_attribute('value') == 'Vitória'


@then ('recebo uma mensagem de erro informando que o nome ja existe')
def step_impl(context):
    br = context.browser
    br.get_screenshot_as_file('/tmp/screenshot.png')
    message = br.find_element_by_id('mensagem').text
    assert br.current_url.endswith('/campus/')
    assert message == "O campus ja existe. Por favor, tente novamente!"

@then('nao conseguirei cadastrar o campus ate que eu o preencha com um nome diferente')
def step_impl(context):
    br = context.browser
    # Checks success status
    assert br.current_url.endswith('/campus/')