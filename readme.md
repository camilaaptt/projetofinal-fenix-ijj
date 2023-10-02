## Bugou? QA Tá ON!
## Projeto Final - Squad Fênix

### Objetivo:

- Você e seu squad são o time de QA responsável pelo teste do sistema de vendas do Instituto Joga Junto. Vocês devem executar testes focados na perspectiva do vendedor.

- Testes automatizados: (pelo menos um cenário testado de modo automatizado).

### Cenários automatizados:
- Cadastro de usuário, utilizando a biblioteca faker;
- Login de usuário já cadastrado.

### Execução dos testes:

##### 1º Passo: Clonar repositório
```
git clone https://github.com/seu-usuario/nome-do-projeto.git
```
##### 2º Passo: Acessar o diretório do projeto
```
cd nome-do-projeto
```
##### 3º Passo: Criar um ambiente virtual e ativar
```bash
python -m venv nomedoambiente

nomedoambiente\Scripts\activate ## Windows
nomedoambiente/bin/activate ##Mac ou Linux
```

##### 4º Passo: Instalar as dependências
Partindo do pressuposto que você já tenha baixado o driver e o navegador atualizado

```bash
pip install selenium behave faker
```

##### 5º Passo: Comando para executar os testes
```
behave
```


