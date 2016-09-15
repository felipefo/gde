from behave import given, when, then
from test.factories.user import UserFactory

@given('I am a logged user')
def step_impl(context):
    br = context.browser
    br.get(context.base_url + '/')

    # Checks for Cross-Site Request Forgery protection input
    assert br.find_element_by_name('csrfmiddlewaretoken').is_enabled()

    # Fill login form and submit it (valid version)
    br.find_element_by_name('username').send_keys('foo')
    br.find_element_by_name('password').send_keys('bar')
    br.find_element_by_name('action').click()

@when('I submit a valid categoria page')
def step_impl(context):
    br = context.browser
    br.get(context.base_url + '/categoria/')

    # Checks for Cross-Site Request Forgery protection input
    assert br.find_element_by_name('csrfmiddlewaretoken').is_enabled()

    # Fill login form and submit it (valid version)
    br.find_element_by_name('nome').send_keys('categoria_teste')
    br.find_element_by_name('submit').click()

@then('I am redirected to the categoria_list page')
def step_impl(context):
    br = context.browser

    # Checks success status
    assert br.current_url.endswith('/categorias_list/')
    # assert br.find_element_by_id('main_title').text == "Login success"
