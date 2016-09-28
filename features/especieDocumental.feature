Feature: Cadastrar EspecieDocumental

  Scenario: Cadastrar nova EspecieDocumental
  Given Eu sou um usuario logado
    And Estou na pagina de cadastro de uma categoria
   When Submeto o cadastro de uma nova categoria
   Then Sou redirecionado para a pagina principal de categorias
    And A categoria esta devidamente cadastrada.
