from behave import given, when, then
from test.factories.user import UserFactory
from app.models import EspecieDocumental

@given('Eu sou um usuario logado')
def step_impl(context):
    #Cria um usuário de teste
    criarNovoUsuario()

    br = context.browser
    br.get(context.base_url + '/')

    # Checks for Cross-Site Request Forgery protection input
    assert br.find_element_by_name('csrfmiddlewaretoken').is_enabled()

    # Fill login form and submit it (valid version)
    br.find_element_by_name('username').send_keys('foo')
    br.find_element_by_name('password').send_keys('bar')
    br.find_element_by_name('action').click()



def criarNovoUsuario():
    # Creates a dummy user for our tests (user is not authenticated at this point)
    u = UserFactory(username='foo', email='foo@example.com')
    u.set_password('bar')
    # Don't omit to call save() to insert object in database
    u.save()

@given('Estou na pagina de cadastro de uma especie documental')
def step_impl(context):
    br = context.browser
    br.get(context.base_url + '/especieDocumental')

    # Checks for Cross-Site Request Forgery protection input
    assert br.find_element_by_name('csrfmiddlewaretoken').is_enabled()
    assert br.current_url.endswith('/especieDocumental/')

@when('Submeto o cadastro de uma nova especie documental deixando o campo em branco')
def step_impl(context):
    br = context.browser

    # Checks for Cross-Site Request Forgery protection input
    assert br.find_element_by_name('csrfmiddlewaretoken').is_enabled()

    # Fill login form and submit it (valid version)
    br.find_element_by_name('submit').click()
    br.get_screenshot_as_file('/tmp/screenshot.png')

@then('Nao conseguirei cadastrar a especie ate que eu preencha o campo nome.')
def step_impl(context):
    br = context.browser
    # br.get_screenshot_as_file('/tmp/screenshot.png')
    # Checks success status
    assert br.current_url.endswith('/especieDocumental/')
    assert br.find_element_by_id('nome').text == ""

@when('Informo um nome ainda nao cadastrado no sistema')
def step_impl(context):
    br = context.browser
    especie = EspecieDocumental.objects.filter(nome='Folha de Ponto').exists()
    assert especie == False

@when('Submeto o cadastro de uma nova especie')
def step_impl(context):
    br = context.browser

    # Checks for Cross-Site Request Forgery protection input
    assert br.find_element_by_name('csrfmiddlewaretoken').is_enabled()

    # Fill login form and submit it (valid version)
    br.find_element_by_name('nome').send_keys('Folha de Ponto')
    br.find_element_by_name('submit').click()
    # br.get_screenshot_as_file('/tmp/screenshot.png')

@then('Sou redirecionado para a pagina principal de especie documental')
def step_impl(context):
    br = context.browser

    # Checks success status
    assert br.current_url.endswith('/especiesDocumentais_list/')

@then('A especie devera estar devidamente cadastrada.')
def step_impl(context):
    br = context.browser

    # Checks success status
    assert br.current_url.endswith('/especiesDocumentais_list/')
    assert br.find_element_by_id('nomeEspecie').text == "Folha de Ponto"

@given('Estou na pagina com a lista de especies documentais')
def step_impl(context):
        br = context.browser
        br.get(context.base_url + '/especiesDocumentais_list')
    # Checks success status
        assert br.current_url.endswith('/especiesDocumentais_list/')

@when('Seleciono o botao editar de uma especie documental')
def step_impl(context):
        br = context.browser
        br.get_screenshot_as_file('/tmp/screenshot.png')
        br.find_element_by_name('editar').click()


@then('Sou redirecionado para a pagina com seus dados')
def step_impl(context):
        br = context.browser


@given('Uma nova especie documental foi criada')
def step_impl(context):
    br=context.browser

    criarNovaEspecieDocumental()

    assert br.find_element_by_name('csrfmiddlewaretoken').is_enabe()

    br.find_element_by_name('nome').send_keys('Ata')
    br.find_element_by_name('submit').click()

def criarNovaEspecieDocumental():
    

@when('Escolho visualizar a lista de especies documentais')
def step_impl(context):
    br = context.browser

    br.get(context.base_url + '/especiesDocumentais_list')
    assert br.current_url.endswith('/especiesDocumentais_list')

@then
def step_impl(context):
    br = context.browser

    assert br.current_url.endswith('/especiesDocumentais_list')
    assert br.find_element_by_id('nomeEspecie').text == 'Ata'