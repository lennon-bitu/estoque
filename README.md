# estoque
### Este mini projeto tem como ideia um controle de estoque onde teremos:
### um cadastro de produtos, cadastro de ajuste no estoque, cadastro de Usuários
### o Usuário precisara esta logado no sistema para fazer fazer as perações de cadastro e alterações

## fitures do sistema
- 1
. :beginner: Produto
    - :beginner: cadastrar
    - :pushpin: editar
    - :pushpin: deletar
    - :white_check_mark: Listar

 - 2
 . :pushpin: Usuário
    - :pushpin: cadastrar
    - :pushpin: editar
    - :pushpin: deletar
    - :pushpin: Listar

- 3
 . :pushpin: estoque
    - :pushpin: Entrada
    - :pushpin: Saida
    - :pushpin: Inventario
    - :pushpin: Listar

### =================================
### 1
 - comando para instalação do Django (com o caminha do projeto aberto e a dentro do ambiente virtual ) execute o comando

 <code> pip install django </code>

### =================================
### 2

- Criação do super usuario
- para criarmos o Super usuario do django precisamos rodar o comando no terminal

<code> python manager.py createsuperuser </code>

- após rodar o camando prenchemos as informações do super usuario
. usuario
. email
. senha
. repetir a senha

### =================================
### 3

- inicializando o projeto django

<code> python manage.py runserver </code>