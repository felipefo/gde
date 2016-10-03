Feature: Funcionalidade EspecieDocumental


  Background:
    Given Eu sou um usuario logado
    And Estou na pagina de cadastro de uma especie documental

  Scenario: Cadastrar campos vazios
   When Submeto o cadastro de uma nova especie documental deixando o campo em branco
   Then Nao conseguirei cadastrar a especie ate que eu preencha o campo nome.

  Scenario: Cadastrar nova EspecieDocumental
   When Informo um nome ainda nao cadastrado no sistema
    And Submeto o cadastro de uma nova especie
   Then Sou redirecionado para a pagina principal de especie documental
    And A especie devera estar devidamente cadastrada.

   When Informo um nome ja cadastrado no sistema
    And Submeto o cadastro de uma nova especie
   Then Recebo uma mensagem de erro informando que o nome ja existe.
    And Nao conseguirei cadastrar a especie ate que eu preencha o com um nome diferente.
