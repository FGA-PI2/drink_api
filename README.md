# drink_api
API restful para o projeto Drinks da disciplina Projeto integrador 2 - FGA 2/2017

# Instalação

Instale o pip.
```apt install python-pip```

Configure sua virtualenv e use-a conforme o [tutorial](http://levipy.com/virtualenv-and-virtualenvwrapper-tutorial/)

Instale as dependencias do projeto:
`pip install -r requirements.txt`


Realize as migrações do banco de dados: 
```
./manage.py makemigrtations
./manage.py migrate 

Para rodar o projeto localmente, execute:
./manage.py runserver [porta] 
```
**[porta] caso em branco o default é 8000** <br />
Acesse `localhost:[porta]` no navegador para ter acesso a API. 
