# API Rest - CRUD de Usuários

API feita utilizando a biblioteca djangorestframework para listagem, inserção, edição e remoção de um modelo chamado Usuário. 

Cada Usuário tem nome, email e telefone.

## Endpoints disponíveis

### - 'users/'
Aceita apenas requisições GET. Retorna um JSON com todos os usuários cadastrados.

### - 'add_user/'
Aceita apenas requisições POST, contendo no corpo da requisição nome, email e telefone. Os dados enviados na requisição irão gerar um cadastro de Usuário. Além disso, como resposta da requisição, retorna os dados do usuário que acaba de ser inserido.

### - 'users/id/'
Aceita apenas requisições GET e retorna um JSON com dados do usuário de id informado.

### - 'delete_user/id/'
Aceita apenas requisições DELETE e deleta do banco de dados o usuário com id informado.

### - 'edit_user/<int:pk>/',
Aceita apenas requisições do tipo PUT, recebendo no corpo da requisição um JSON contendo qual dado deseja alterar, exemplo "{'nome': 'Fulano', 'telefone': '(11) 98765-4321}" de modo que o usuário com id informado terá seu nome alterado para 'Fulano' e telefone alterado também. Caso seja necessário editar mais ou menos campos, basta adicionar ou remover na requisição o campo informado juntamente com o valor correspondente. 

## Como executar

- Faça o clone do repositório: git clone https://github.com/Gabriel-Rezende/crud-users-api.git
- Entre na pasta bridgehub:  cd .\crud-users-api\bridgehub\
- Ative uma venv: source venv/bin/activate
- Instale os requirements: pip3 install -r requirements.txt
- Execute: python manage.py runserver
- Para testar, use: python manage.py test

- Após isso, será executado no seu localhost na porta 8000 a API. Requisições deverão ser feitas na URL base 'http:127.0.0.1:8000/' colocando o endpoint na frente. Exemplo: 'http:127.0.0.1:8000/users/'
