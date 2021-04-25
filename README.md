<img src="https://img.shields.io/static/v1?label=Python&message=Django&color=7159c1&style=for-the-badge&logo=python"/>


# Super-Heroes
* API criada para salvar herois em base de dados e verificar o ganhador em uma luta entre eles

<!--ts-->
   * [Sobre](#super-heroes)
   * [Tabela de Conteudo](#tabela-de-conteudo)
   * [Requisitos](#Requisitos)
   * [Iniciando Aplicação](#iniciando-aplicação)
   * [Rotas](#rotas)
   * [Tecnologias](#tecnologias)
<!--te-->

# Requisitos
* Requisitos para utilizar essa aplicação localmente são:
    * Python de preferencia na versão 3.9
    * Banco de dados PSQL
    * Pip em sua versão atualizada

# Configurações necessárias
* algumas configurações são necessárias para utilizar essa aplicação:
    * Criar uma base de dados no postgresql
    * Em super_heroes/settings na variavel DATABASES trocar os parametros 'NAME','USER','PASSWORD' para o nome da base de dados, usuário postgre e senha desse usuário.
    * Pelo terminal na pasta do projeto rodar sem aspas "pip install -r requirements.txt"
    * Ainda no terminal rode o comando "./manage.py migrate" para aplicar configurações em base de dados

# Iniciando aplicação
* comando para iniciar "./manage.py runserver"
* O servidor inciará na porta:8000 - acesse <http://localhost:8000> 

# Status
<h4 align="center"> 
	☢  Projeto está na fase alpha  ☢
</h4>

# Rotas
## /Character/
## GET
* Parametros ?name='name'
### Body
```json
no body
```
### Response
```json
[
  {
    "id": 1,
    "name": "Superman",
    "photo": "http://localhost:8000/static/download_MdzCXxF.jpeg",
    "description": "descrição",
    "universe": "DC",
    "height": "1.91",
    "weight": "101",
    "strength": 10,
    "speed": 10
  },
  {
    "id": 2,
    "name": "batman",
    "photo": "http://localhost:8000/static/batman.jpeg",
    "description": "descrição",
    "universe": "DC",
    "height": "1.82",
    "weight": "80",
    "strength": 5,
    "speed": 3
  },
  ...
]
```
## POST
* must be a multipart to post a image file.
### Body
```json
{
    "name": "Superman",
    "photo": IMAGE_FILE,
    "description": "descrição",
    "universe": "DC",
    "height": "1.91",
    "weight": "101",
    "strength": 10,
    "speed": 10
},
```
### Response
```json
[
  {
    "id": 1,
    "name": "Superman",
    "photo": "http://localhost:8000/static/download_MdzCXxF.jpeg",
    "description": "descrição",
    "universe": "DC",
    "height": "1.91",
    "weight": "101",
    "strength": 10,
    "speed": 10
  },
  ...
]
```
## /Character/{id}
## GET
### Body
```json
no body
```
### Response
```json

{
    "id": 3,
    "name": "batman",
    "photo": "/static/batman.jpeg",
    "description": "descrição",
    "universe": "DC",
    "height": "1.82",
    "weight": "80",
    "strength": 5,
    "speed": 3
}

```
## PUT
* must be multipart for photo
### Header
```json
auth-token: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjo0LCJ1c2VybmFtZSI6ImthaW9zZXIiLCJleHAiOjE2MTkyNzc2NzMsImVtYWlsIjoia2Fpb0BlbWFpbC5jb20ifQ.SDZ36RMTmUgjUTwGnKOsjTAWUniwLxPdDXafJvi94QA
```
### Body
```json
{
    "name": "Homem de ferro",
    "photo": PHOTO FILE,
    "description": "descrição",
    "universe": "MARVEL",
    "height": "1.68",
    "weight": "67",
    "strength": 6,
    "speed": 7
}
```
### Response
```json
{
    "id": 3,
    "name": "Homem de ferro",
    "photo": PHOTO FILE,
    "description": "descrição",
    "universe": "MARVEL",
    "height": "1.68",
    "weight": "67",
    "strength": 6,
    "speed": 7
}
```

## PATCH
### Header
```json
auth-token: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjo0LCJ1c2VybmFtZSI6ImthaW9zZXIiLCJleHAiOjE2MTkyNzc2NzMsImVtYWlsIjoia2Fpb0BlbWFpbC5jb20ifQ.SDZ36RMTmUgjUTwGnKOsjTAWUniwLxPdDXafJvi94QA
```
### Body
```json
{
    "name": "Cat Girl",
},
```
### Response
```json
{
    "id": 4,
    "name": "Cat Girl",
    "photo": "/static/super.jpg",
    "description": "descrição",
    "universe": "DC",
    "height": "1.60",
    "weight": "50",
    "strength": 7,
    "speed": 6
  }
}
```

## DELETE
### Body
```json
NO BODY
```
### Response
```json
STATUS 204 NO CONTENT
```

## /Character/favorites/
## GET
### Header
```json
auth-token: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjo0LCJ1c2VybmFtZSI6ImthaW9zZXIiLCJleHAiOjE2MTkyNzc2NzMsImVtYWlsIjoia2Fpb0BlbWFpbC5jb20ifQ.SDZ36RMTmUgjUTwGnKOsjTAWUniwLxPdDXafJvi94QA
```
### Body
```json
no body
```
### Response
```json
[
  {
    "id": 11,
    "character": {
      "id": 3,
      "name": "batman",
      "photo": "/static/batman.jpeg",
      "description": "descrição",
      "universe": "DC",
      "height": "1.82",
      "weight": "80",
      "strength": 5,
      "speed": 3
    },
    "user": {
      "id": 4,
      "username": "kaioser",
      "first_name": "Kaio Henrique",
      "last_name": "Oliveira da Silva",
      "email": "kaio@email.com"
    }
  },
  {
    "id": 12,
    "character": {
      "id": 4,
      "name": "super shock",
      "photo": "/static/super.jpg",
      "description": "descrição",
      "universe": "DC",
      "height": "1.60",
      "weight": "50",
      "strength": 7,
      "speed": 6
    },
    "user": {
      "id": 4,
      "username": "kaioser",
      "first_name": "Kaio Henrique",
      "last_name": "Oliveira da Silva",
      "email": "kaio@email.com"
    }
  },
  ...
]
```
## POST
### Header
```json
auth-token: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjo0LCJ1c2VybmFtZSI6ImthaW9zZXIiLCJleHAiOjE2MTkyNzc2NzMsImVtYWlsIjoia2Fpb0BlbWFpbC5jb20ifQ.SDZ36RMTmUgjUTwGnKOsjTAWUniwLxPdDXafJvi94QA
```
### Body
```json
{
    "character_id":4
},
```
### Response
```json
{
  "id": 12,
  "character": {
    "id": 4,
    "name": "super shock",
    "photo": "/static/super.jpg",
    "description": "descrição",
    "universe": "DC",
    "height": "1.60",
    "weight": "50",
    "strength": 7,
    "speed": 6
  },
  "user": {
    "id": 4,
    "username": "kaioser",
    "first_name": "Kaio Henrique",
    "last_name": "Oliveira da Silva",
    "email": "kaio@email.com"
  }
}
```
## /Character/favorites/{id}
## GET
### Header
```json
auth-token: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjo0LCJ1c2VybmFtZSI6ImthaW9zZXIiLCJleHAiOjE2MTkyNzc2NzMsImVtYWlsIjoia2Fpb0BlbWFpbC5jb20ifQ.SDZ36RMTmUgjUTwGnKOsjTAWUniwLxPdDXafJvi94QA
```
### Body
```json
no body
```
### Response
```json

{
    "id": 1,
    "character": {
      "id": 3,
      "name": "batman",
      "photo": "/static/batman.jpeg",
      "description": "descrição",
      "universe": "DC",
      "height": "1.82",
      "weight": "80",
      "strength": 5,
      "speed": 3
    },
    "user": {
      "id": 4,
      "username": "kaioser",
      "first_name": "Kaio Henrique",
      "last_name": "Oliveira da Silva",
      "email": "kaio@email.com"
    }
}

```
## PUT
### Header
```json
auth-token: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjo0LCJ1c2VybmFtZSI6ImthaW9zZXIiLCJleHAiOjE2MTkyNzc2NzMsImVtYWlsIjoia2Fpb0BlbWFpbC5jb20ifQ.SDZ36RMTmUgjUTwGnKOsjTAWUniwLxPdDXafJvi94QA
```
### Body
```json
{
    "character": {
      "id": 3,
      "name": "batman",
      "photo": "/static/batman.jpeg",
      "description": "descrição",
      "universe": "DC",
      "height": "1.82",
      "weight": "80",
      "strength": 5,
      "speed": 3
    },
    "user": {
      "id": 3,
      "username": "kaiouser",
      "first_name": "Kaio Henrique",
      "last_name": "Oliveira da Silva",
      "email": "kaio@email.com"
    }
},
```
### Response
```json
{
    "id":4,
    "character": {
      "id": 3,
      "name": "batman",
      "photo": "/static/batman.jpeg",
      "description": "descrição",
      "universe": "DC",
      "height": "1.82",
      "weight": "80",
      "strength": 5,
      "speed": 3
    },
    "user": {
      "id": 3,
      "username": "kaiouser",
      "first_name": "Kaio Henrique",
      "last_name": "Oliveira da Silva",
      "email": "kaio@email.com"
    }
},
```

## PATCH
### Header
```json
auth-token: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjo0LCJ1c2VybmFtZSI6ImthaW9zZXIiLCJleHAiOjE2MTkyNzc2NzMsImVtYWlsIjoia2Fpb0BlbWFpbC5jb20ifQ.SDZ36RMTmUgjUTwGnKOsjTAWUniwLxPdDXafJvi94QA
```
### Body
```json
{
    "character": {
        "id": 4,
        "name": "super shock",
        "photo": "/static/super.jpg",
        "description": "descrição",
        "universe": "DC",
        "height": "1.60",
        "weight": "50",
        "strength": 7,
        "speed": 6
    }
},
```
### Response
```json
{
  "id": 4,
  "character": {
    "id": 4,
    "name": "super shock",
    "photo": "/static/super.jpg",
    "description": "descrição",
    "universe": "DC",
    "height": "1.60",
    "weight": "50",
    "strength": 7,
    "speed": 6
  }
}
```

## DELETE
### Header
```json
auth-token: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjo0LCJ1c2VybmFtZSI6ImthaW9zZXIiLCJleHAiOjE2MTkyNzc2NzMsImVtYWlsIjoia2Fpb0BlbWFpbC5jb20ifQ.SDZ36RMTmUgjUTwGnKOsjTAWUniwLxPdDXafJvi94QA
```
### Body
```json
NO BODY
```
### Response
```json
STATUS 204 NO CONTENT
```

## /Character/fight/
## POST
### Body
```json
{
    "character_1":2,
    "character_2":3,
}

```
### Response
```json
"grande vitória do Superman"
```
## /Character/fight/
## POST
### Body
```json
{
    "username":"kaioser",
    "password":"123456",
}

```
### Response
```json
{
    "token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjo0LCJ1c2VybmFtZSI6ImthaW9zZXIiLCJleHAiOjE2MTkyNzc2NzMsImVtYWlsIjoia2Fpb0BlbWFpbC5jb20ifQ.SDZ36RMTmUgjUTwGnKOsjTAWUniwLxPdDXafJvi94QA",
}
```
## /Character/user/
## GET
### Body
```json
NO BODY CONTENT
```
### Response
```json
[
  {
    "id": 1,
    "username": "kaio",
    "first_name": "",
    "last_name": "",
    "email": ""
  },
  {
    "id": 3,
    "username": "kaiouser",
    "first_name": "Kaio Henrique",
    "last_name": "Oliveira da Silva",
    "email": "kaio@email.com"
  },
  {
    "id": 4,
    "username": "kaioser",
    "first_name": "Kaio Henrique",
    "last_name": "Oliveira da Silva",
    "email": "kaio@email.com"
  }
]
```
## GET
### Header
```json
auth-token: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjo0LCJ1c2VybmFtZSI6ImthaW9zZXIiLCJleHAiOjE2MTkyNzc2NzMsImVtYWlsIjoia2Fpb0BlbWFpbC5jb20ifQ.SDZ36RMTmUgjUTwGnKOsjTAWUniwLxPdDXafJvi94QA
```
### BODY
```json
{
    "email": "kaiooliver@email.com"
}
```
### Response
```json

{
    "id": 4,
    "username": "kaioser",
    "first_name": "Kaio Henrique",
    "last_name": "Oliveira da Silva",
    "email": "kaiooliver@email.com"
}

```
## DELETE
### Header
```json
auth-token: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjo0LCJ1c2VybmFtZSI6ImthaW9zZXIiLCJleHAiOjE2MTkyNzc2NzMsImVtYWlsIjoia2Fpb0BlbWFpbC5jb20ifQ.SDZ36RMTmUgjUTwGnKOsjTAWUniwLxPdDXafJvi94QA
```
### Body
```json
NO BODY
```
### Response
```json
STATUS 204 NO CONTENT
```
## DELETE
### Body
```json
{
    "username": "usuario",
    "password": "123456",
    "first_name": "Jorge",
    "last_name": "Fonseca",
    "email": "jorge@email.com"
}
```
### Response
```json
{
    "username": "usuario",
    "first_name": "Jorge",
    "last_name": "Fonseca",
    "email": "jorge@email.com"
}, 201 CREATED
```
