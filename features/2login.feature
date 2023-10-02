# language: pt
Funcionalidade: Fluxo de Login/Logout
    
    Como vendedor cadastrado do e-commerce do Instituto Joga Junto
    Eu quero realizar meu login no e-commerce, a partir do meu computador
    Para ter acesso ao site.

  Cenário: Login com sucesso
    Dado que eu acesse o site do Instituto Joga Junto
    Quando eu preencher os dados no formulario de login
    Então devo visualizar a mensagem 'logado com sucesso'