# language: pt
Funcionalidade: Cadastro de Usuário
    
    Como vendedor do e-commerce do Instituto Joga Junto
    Eu quero realizar meu cadastro no e-commerce
    Para ter acesso ao site.

  Cenário: Cadastro com sucesso
    Dado que eu acesse o site de cadastro no e-commerce do Instituto Joga Junto
    Quando eu preencher os dados no formulario de cadastro
    Então devo visualizar a mensagem 'Usuário cadastrado com sucesso'