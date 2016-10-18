Feature: Funcionalidade Campus


  Background: Em todos os testes o usuário deve estar logado.
    Given Eu sou um usuario logado

  Scenario: Cadastrar um novo campus
    Given que eu estou na pagina de cadastrar campus
    And Informo um nome ainda nao cadastrado no sistema
    When clico no botão enviar
    Then sou redirecionado para a pagina com a lista de campi cadastrados
    And o campus deve estar devidamento cadastrado

    Given que eu estou na pagina de cadastrar campus
    And preencho o nome do campus em branco
    When clico no botão enviar
    Then nao conseguirei cadastrar o campus ate que eu preencha o campo nome

    Given que eu estou na pagina de cadastrar campus
    And informo um nome ja cadastrado no sistema
    When clico no botão enviar
    Then recebo uma mensagem de erro informando que o nome ja existe
    And nao conseguirei cadastrar o campus ate que eu o preencha com um nome diferente