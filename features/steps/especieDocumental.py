from behave import given, when, then
from test.factories.user import UserFactory

@given('I am a logged user')
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


@when('I submit a valid especieDocumental page')
def step_impl(context):
    br = context.browser
    br.get(context.base_url + '/especieDocumental')

    # Checks for Cross-Site Request Forgery protection input
    assert br.find_element_by_name('csrfmiddlewaretoken').is_enabled()
    
    # Fill login form and submit it (valid version)
    br.find_element_by_name('nome').send_keys('Folha de Ponto')
    br.find_element_by_name('submit').click()
    # br.get_screenshot_as_file('/tmp/screenshot.png')


@then('I am redirected to the especieDocumental_list page')
def step_impl(context):
    br = context.browser

    # Checks success status
    assert br.current_url.endswith('/especiesDocumentais_list/')
    assert br.find_element_by_id('nomeEspecie').text == "Folha de Ponto"
