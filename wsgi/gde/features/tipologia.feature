Feature: Funcionalidade Tipologia

  Background: Em todos os testes o usuário deve estar logado.
    Given Eu sou um usuario logado
    Given Estou na pagina principal do sistema
  Scenario: Listar meus levantamentos
    When Clico na opcao Meus Levantamentos
    Then sou redirecionado para a pagina com a lista de levantamentos feitos pelo usuario
    And Devem ser listados todos os levantamentos já cadastrados no sistema.