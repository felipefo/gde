from behave import given, when, then

#Scenario: Campos Vazios
@given('Estou na pagina de cadastro de um setor')
def step_impl(context):
    br = context.browser
    br.get(context.base_url + '/setor')

    # Checks for Cross-Site Request Forgery protection input
    assert br.find_element_by_name('csrfmiddlewaretoken').is_enabled()
    assert br.current_url.endswith('/setor/')

@when('Submeto o cadastro de um novo setor deixando algum campo em branco')
def step_impl(context):
    br = context.browser

    # Checks for Cross-Site Request Forgery protection input
    assert br.find_element_by_name('csrfmiddlewaretoken').is_enabled()

    # Fill login form and submit it (valid version)
    br.find_element_by_name('submit').click()

@then('Nao conseguirei cadastrar o setor ate que eu preencha o campo nome.')
def step_impl(context):
    br = context.browser
    # br.get_screenshot_as_file('/tmp/screenshot.png')
    # Checks success status
    assert br.current_url.endswith('/setor/')
    assert br.find_element_by_id('nome').text == ""





#Scenario: Cadastrar novo setor
@when('Informo um campus, nome, sigla, funcao, atividades  e historico')
def step_impl(context):
    br = context.browser

    # Checks for Cross-Site Request Forgery protection input
    assert br.find_element_by_name('csrfmiddlewaretoken').is_enabled()

    br.find_element_by_name('nome').send_keys('setorTeste')
    br.find_element_by_name('sigla').send_keys('ST')
    br.find_element_by_name('funcao').send_keys('funcao')
    br.find_element_by_name('atividade').send_keys('atividade1')
    br.find_element_by_name('SubmitAtividade').click()
    br.find_element_by_name('historico').send_keys('historico1')
    br.find_element_by_name('SubmitHistórico').click()
    br.find_element_by_name('submit').click()

@when('Não existir setor com mesmo nome e sigla já cadastrado para o campus escolhido')
def step_impl(context):
    br = context.browser

    # Checks for Cross-Site Request Forgery protection input
    assert br.find_element_by_name('csrfmiddlewaretoken').is_enabled()

    # Fill login form and submit it (valid version)
    br.find_element_by_name('submit').click()

@when('Submeto o cadastro de um novo setor')
def step_impl(context):
    br = context.browser

    # Checks for Cross-Site Request Forgery protection input
    assert br.find_element_by_name('csrfmiddlewaretoken').is_enabled()

    # Fill login form and submit it (valid version)
    br.find_element_by_name('submit').click()

@then('Sou redirecionado para a pagina principal de setor')
def step_impl(context):
    br = context.browser
    # br.get_screenshot_as_file('/tmp/screenshot.png')
    # Checks success status
    assert br.current_url.endswith('/setor/')
    assert br.find_element_by_id('nome').text == ""

@then('O setor devera estar devidamente cadastrado.')
def step_impl(context):
    br = context.browser
    # br.get_screenshot_as_file('/tmp/screenshot.png')
    # Checks success status
    assert br.current_url.endswith('/setor/')
    assert br.find_element_by_id('nome').text == ""