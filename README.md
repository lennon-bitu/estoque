# estoque
### Este mini projeto tem como ideia um controle de estoque onde teremos:
### um cadastro de produtos, cadastro de ajuste no estoque, cadastro de Usuários
### o Usuário precisara esta logado no sistema para fazer fazer as perações de cadastro e alterações

## funcionalidades do sistema
- 1
    - views criadas usando fbv (function basic view)
. :beginner: Produto
    - :white_check_mark: cadastrar
    - :white_check_mark: editar
    - :white_check_mark: deletar
    - :white_check_mark: Listar

 - 2
    - views criadas usando cbv (class basic view)
 . :beginner: Usuário
    - :pushpin: cadastrar
    - :pushpin: editar
    - :pushpin: deletar
    - :pushpin: Listar

- 3
    - views criadas usando cbv (class basic view)
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