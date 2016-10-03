Feature: funcionalidade EspecieDocumental

  Scenario: Cadastrar nova EspecieDocumental
  Given Eu sou um usuario logado
    And Estou na pagina de cadastro de uma categoria
   When Submeto o cadastro de uma nova categoria
   Then Sou redirecionado para a pagina principal de categorias
    And A categoria esta devidamente cadastrada.

  Scenario:  Editar Especie documental
  Given  Eu sou um usuario logado
    And  Estou na pagina com a lista de especies documentais
    When Seleciono o botao editar de uma especie documental
    Then Sou redirecionado para a pagina com seus dados

