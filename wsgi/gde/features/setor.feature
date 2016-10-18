Feature: Funcinalidade Setor

  Background: Em todos os testes o usuário deve estar logado.
    Given Eu sou um usuario logado

  Scenario: Cadastrar campos vazios
  Given Estou na pagina de cadastro de um setor
   When Submeto o cadastro de um novo setor deixando algum campo em branco
   Then Nao conseguirei cadastrar o setor ate que eu preencha o campo nome.

 Scenario: Cadastrar novo setor
  Given Estou na pagina de cadastro de um setor
   When Informo um nome, sigla e campus
    And Não existir setor com mesmo nome e sigla já cadastrado para o campus escolhido
    And Submeto o cadastro de um novo setor
   Then Sou redirecionado para a pagina principal de setor
    And O setor devera estar devidamente cadastrado.