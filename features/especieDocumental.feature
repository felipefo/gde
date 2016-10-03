
Feature: Funcionalidade EspecieDocumental

  Scenario: Cadastrar campos vazios
  Given Eu sou um usuario logado
    And Estou na pagina de cadastro de uma especie documental
   When Submeto o cadastro de uma nova especie documental deixando o campo em branco
   Then Nao conseguirei cadastrar a especie ate que eu preencha o campo nome.

  Scenario: Cadastrar nova EspecieDocumental
  Given Eu sou um usuario logado
    And Estou na pagina de cadastro de uma especie documental
   When Informo um nome ainda nao cadastrado no sistema
    And Submeto o cadastro de uma nova especie
   Then Sou redirecionado para a pagina principal de especie documental
    And A especie devera estar devidamente cadastrada.

  Scenario:  Editar Especie documental
  Given Eu sou um usuario logado
    And Estou na pagina com a lista de especies documentais
    And Possue uma ou mais especies documentais cadastradas
   When Seleciono o botao editar de uma especie documental
    And Sou redirecionado para a pagina com seus dados ja preenchidos
    And Preencho os campos obrigatorios
    And Clico no botao salvar
   Then Sou redirecionado para a pagina principal de especie documental