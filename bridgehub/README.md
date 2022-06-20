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
