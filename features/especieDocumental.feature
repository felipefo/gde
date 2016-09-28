Feature: Funcionalidade EspecieDocumental

  Scenario: Cadastrar campos vazios
  Given Eu sou um usuario logado
    And Estou na pagina de cadastro de uma especie documental
   When Submeto o cadastro de uma nova especie documental deixando o campo em branco
   Then Nao conseguirei cadastrar a especie ate que eu preencha o campo nome.

  Scenario: Cadastrar nova EspecieDocumental
  Given Eu sou um usuario logado
    And Estou na pagina de cadastro de uma especie documental
   When Submeto o cadastro de uma nova especie
   Then Sou redirecionado para a pagina principal de especie documental
    And A especie devera devidamente cadastrada.
