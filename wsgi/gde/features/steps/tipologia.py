from behave import given, when, then
from test.factories.tipologia import TipologiaFactory
from test.factories.fase import FaseFactory


@when('Clico na opcao Meus Levantamentos')
def step_impl(context):

    fase = FaseFactory(nome='Levantamento')
    tipologia = TipologiaFactory()
    assert tipologia.nome == 'Nome da Tipologia 000'
    # assert tipologia.fase == 'Levantamento'

@then('sou redirecionado para a pagina com a lista de levantamentos feitos pelo usuario')
def step_impl(context):
    pass

@then('Devem ser listados todos os levantamentos já cadastrados no sistema.')
def step_impl(context):
    pass