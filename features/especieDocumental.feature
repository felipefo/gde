Feature: Cadastrar Categoria

  Scenario: Add a new Categoria
  Given I am a logged user
  When I submit a valid categoria page
  Then I am redirected to the categoria_list page
