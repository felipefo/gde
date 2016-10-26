from behave import given, when, then
from app.models import Campus
from test.factories.campus import CampusFactory


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
    assert br.find_element_by_id('id_nome').get_attribute('value') == 'Vitória'

@when('clico no botão enviar')
def step_impl(context):
        br = context.browser
        assert br.find_element_by_name('csrfmiddlewaretoken').is_enabled()
        br.find_element_by_name('submit').click()
        #br.get_screenshot_as_file('/tmp/screenshot.png')

@then('o campus deve estar devidamento cadastrado')
def step_impl(context):
    br = context.browser

    # Checks success status
    assert br.current_url.endswith('/campi_list/')
    assert br.find_element_by_id('nomeCampus').text == "Vitória"

@given('preencho o nome do campus em branco')
def step_impl(context):
        br = context.browser
        br.find_element_by_id('id_nome').clear()
        assert br.find_element_by_id('id_nome').get_attribute('value') == ""

@then('nao conseguirei cadastrar o campus ate que eu preencha o campo nome')
def step_impl(context):
    br = context.browser
    # Checks success status
    assert br.current_url.endswith('/campus/')
    assert br.find_element_by_id('id_nome').text == ""

@given('informo um nome ja cadastrado no sistema')
def step_impl(context):
    br = context.browser
    br.get(context.base_url + '/campus')
    especie = Campus.objects.filter(nome='Vitória').exists()
    br.find_element_by_id('id_nome').send_keys('Vitória')
    assert  especie == True
    assert br.find_element_by_id('id_nome').get_attribute('value') == 'Vitória'


@then ('recebo uma mensagem de erro informando que o nome ja existe')
def step_impl(context):
    br = context.browser
    #br.get_screenshot_as_file('/tmp/screenshot.png')
    message = br.find_element_by_class_name('errorlist').text
    campus = Campus.objects.all()
    assert br.current_url.endswith('/campus/%d/edit/' % campus[0].id)
    assert message == "Campus com este Nome já existe."

@then ('recebo uma mensagem de erro informando que este nome ja existe')
def step_impl(context):
    br = context.browser
    #br.get_screenshot_as_file('/tmp/screenshot.png')
    message = br.find_element_by_class_name('errorlist').text
    assert br.current_url.endswith('/campus/')
    assert message == "Campus com este Nome já existe."

@then ('recebo uma mensagem de erro informando que o campo e obrigatorio')
def step_impl(context):
    br = context.browser
    #br.get_screenshot_as_file('/tmp/screenshot.png')
    message = br.find_element_by_class_name('errorlist').text
    campus = Campus.objects.all()
    assert br.current_url.endswith('/campus/%d/edit/' % campus[0].id)
    assert message == "Este campo é obrigatório."

@then('nao conseguirei cadastrar o campus ate que eu o preencha com um nome diferente')
def step_impl(context):
    br = context.browser
    # Checks success status
    assert br.current_url.endswith('/campus/')

@given('Estou na pagina com a lista de campus')
def step_impl(context):
    br = context.browser
    br.get(context.base_url + '/campi_list')
    assert br.current_url.endswith('/campi_list/')

@given('Possui um ou mais campus cadastrados')
def step_impl(context):
    br = context.browser
    campusFactory(2)
    qtdCampus = len(Campus.objects.all())
    assert qtdCampus > 0

def campusFactory(quantidade):
    for index in range(quantidade):
        nomeCampus = 'campus' + str(index)
        campus = CampusFactory(nome=nomeCampus)
        campus.save()

@given('Seleciono o botao editar de um campus')
def step_impl(context):
        br = context.browser
        br.get(context.base_url + '/campi_list')
        br.find_element_by_name('editar').click()

@given('Sou redirecionado para a pagina com seus dados do campus ja preenchidos')
def step_impl(context):
        br = context.browser
        campus = Campus.objects.all()
        br.get(context.base_url + '/campus/%d/edit' % campus[0].id)
        assert br.current_url.endswith('/campus/%d/edit/' % campus[0].id)

@given('Edito o campo campus e o deixo em branco')
def step_impl(context):
        br = context.browser
        br.find_element_by_id('id_nome').clear()
        assert br.find_element_by_id('id_nome').get_attribute('value') == ""

@then('Nao conseguirei editar campus ate que preencha o campo nome')
def step_impl(context):
        br = context.browser
    # br.get_screenshot_as_file('/tmp/screenshot.png')
    # Checks success status
        campus = Campus.objects.all()
        assert br.current_url.endswith('/campus/%d/edit/' % campus[0].id)
        assert br.find_element_by_id('id_nome').text == ""

@given('Edito o nome do campus e coloco um nome que ja esta cadastrado')
def step_impl(context):
        br = context.browser
        campi = Campus.objects.all()
        assert  len(campi) > 1
        nome = campi[1].nome
        br.find_element_by_id('id_nome').clear()
        br.find_element_by_id('id_nome').send_keys(nome)
        assert br.find_element_by_id('id_nome').get_attribute('value') == nome

@given('Nao altero o campus deixando com o nome ja preenchido')
def step_impl(context):
        br = context.browser
        campi = Campus.objects.all()
        assert br.find_element_by_id('id_nome').get_attribute('value') == campi[0].nome

@then('Nao conseguirei salvar o campus ate que eu o preencha com um nome diferente.')
def step_impl(context):
        br = context.browser
        #br.get_screenshot_as_file('/tmp/screenshot.png')
    # Checks success status
        campi = Campus.objects.all()
        assert br.current_url.endswith('/campus/%d/edit/' % campi[0].id)
        assert br.find_element_by_id('id_nome').text == ""

@given('Um campus foi cadastrado')
def step_impl(context):
    br = context.browser
    campusFactory(1)
    campi = Campus.objects.all()
    assert len(campi) > 0

@then('sou redirecionado para a pagina com a lista de campi cadastrados')
def step_impl(context):
    br = context.browser

    # Checks success status
    assert br.current_url.endswith('/campi_list/')

@when('sou redirecionado para a pagina com a lista de campi cadastrados')
def step_impl(context):
    br = context.browser
    br.get(context.base_url + '/campi_list/')
    # Checks success status
    assert br.current_url.endswith('/campi_list/')

@then('O campus devera aparecer na lista.')
def step_impl(context):
    br = context.browser

    # Checks success status
    assert br.current_url.endswith('/campi_list/')
    assert br.find_element_by_id('nomeCampus').text == "campus0"


@when('clico no botao visualizar campus')
def step_impl(context):
    br = context.browser
    br.find_element_by_name('visualizarCampus').click()
    assert br.current_url.endswith('/campi_list/')

@given('que existem campi cadastrados')
def step_impl(context):
        br = context.browser
        campusFactory(3)
        br.refresh()
        campus = Campus.objects.all()
        assert len(campus) == 3
        assert br.current_url.endswith('/campi_list/')


@when('clico no botao excluir.')
def step_impl(context):
    br = context.browser
    br.get_screenshot_as_file('/tmp/screenshot.png')
    br.find_element_by_name('excluir').click()
    assert br.current_url.endswith('/campi_list/')

@then('o campus deixara de existir.')
def step_impl(context):
        br = context.browser

        br.refresh()
        assert Campus.objects.count() == 2

@given('Possui um ou mais campi cadastrados')
def step_impl(context):
    campusFactory(2)
    br = context.browser
    qtdEspecie = len(Campus.objects.all())
    assert qtdEspecie > 0



@then('Sou redirecionado para a pagina principal do campus')
def step_impl(context):
    br = context.browser

    # Checks success status
    assert br.current_url.endswith('/campi_list/')

@given('Preencho o campo campus com um novo nome')
def step_impl(context):
        br = context.browser
        novo_nome = 'novo nome'
        especie = Campus.objects.filter(nome=novo_nome).exists()
        assert especie == False
        br.find_element_by_id('id_nome').clear()
        nome = br.find_element_by_id('id_nome').send_keys(novo_nome)
        assert br.find_element_by_id('id_nome').get_attribute('value') == novo_nome
