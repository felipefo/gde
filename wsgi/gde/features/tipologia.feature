Feature: Funcinalidade Tipologia
  
  Background: Em todos os testes o usuário deve estar logado.
    Given Eu sou um usuario logado
    
 Scenario: Cadastrar novo tipologia
  Given Estou na pagina de cadastro de uma tipologia
   When Informo os dados do formulario
    And Nao existir uma tipologia com os mesmos dados ja cadastrado
    And Submeto o cadastro de uma nova tipologia
   Then Sou redirecionado para a pagina principal do sistema
    And A tipologia devera estar devidamente cadastrado.

  Given Estou na pagina de cadastro de uma tipologia
   When Informo uma tipologia ja cadastrado no sistema
    And Submeto o cadastro de uma nova tipologia
   Then Recebo uma mensagem de erro informando que a tipologia ja existe.
    And Nao conseguirei cadastrar a tipologia ate que eu preencha com dados diferentes.


