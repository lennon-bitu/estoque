# estoque
# ======================================================================================================================================
# 1

# comando para instalação do Django

# <cmd> pip install django </cmd>

# ======================================================================================================================================
# 2

# comando para criar um projeto django colocamos o ponto no final do comando
# paraque o projeto seja criado em apenas uma pasta e não criar a subpasta como
# o mesmo nome do projeto

<code> django-admin startproject nomedoprojeto . </code>

# ======================================================================================================================================
# 3

# comando para criar os Apps, para o django os apps são como modulos que serão
# adicionado ao sistema
# como por exemplo para um aplicativo de estoque podemos ter os modulos de produto
# e o modulo de estoque onde os dois se comunicarão atravez de uma aplicação core (um tipo de main onde fara as comunicação dos apps)

<code> django-admin startapp nomedoapp </code>

# ======================================================================================================================================
# 4

# Criação do super usuario
# para criarmos o Super usuario do django precisamos rodar o comando

<code> python manager.py createsuperuser </code>

# após rodar o camando prenchemos as informações do super usuario
# usuario
# email
# senha
# repetir a senha

# ======================================================================================================================================
# 5

# após a criação de nossos Apps e necessario incluir o mesmo na inicialização do nosso projeto
# indo ate o arquivo seting do projeto
# procurando o trecho de codigo onde esta a inicialização dos app e adicionando os app a este trecho
# ======================================================================================================================================
# 6
# inicializando o projeto django

<code> python manage.py runserver </code>

# esse comando inicialmente vai exibir uma pagina padrão criada junto com o projeto django onde tem alguns informação sobre o Django