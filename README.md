# API de catalogos

O Problema a ser resolvido:

Como administrador de uma plataforma de exibição de filmes, documentarios ou séries, quero poder administrar categorias, generos, elenco e os videos em uma pagina administrativa.

## Regras de negócio

Por ordem de prioridade

### Categorias

- [ ] O administrador pode criar, recuperar, listar, atualizar e deletar as categorias de um video

![Diagrama de classes](https://megustaviajar.sfo2.cdn.digitaloceanspaces.com/category_cass_diagram.png)

Criar uma categoria

![Criar uma categoria](https://megustaviajar.sfo2.cdn.digitaloceanspaces.com/use_case_create_category.png)

![Criar uma categoria via http](https://megustaviajar.sfo2.cdn.digitaloceanspaces.com/use_case_create_category_http.png)

### Generos

- [ ] O administrador pode criar, recuperar, listar, atualizar e deletar as generos de um video

### Videos

- [ ] O administrador pode criar, recuperar, listar, atualizar e deletar um video

  - [ ] Ao criar um video uma categoria ou genero não podem estar deletadas ou inativas

  - [ ] Ao criar o administrador pode fazer upload 4 arquivos: uma thumbnail, uma imagem de capa, um trailler, o video completo

  - [ ] Ao deletar um video estes devem ser excluidos da cdn assim como suas variações. Ex: thumbnails_x_y.ext, videos_xyz_144p.ext, videos_xyz_240p.ext, videos_xyz_360p.ext ...

### Elenco

- [ ] O administrador pode criar, recuperar, listar, atualizar e deletar o elenco de um video

## Requisitos técnicos

- [ ] O upload de uma thumbnail e imagem de capa devem aceitar apenas a extensões `image/*`

- [ ] O upload de umm video deve aceitar apenas as extensões `video/*`

- [ ] Os arquivos devem ser enviados para uma cdn como a AWS S3 ou Google Cloud Storage ou Digital Ocean Spaces

- [ ] Após persistir o video no banco de dados e após os uploads terem sido completados deve-se publicar uma mensagem para uma fila com os seguintes dados

```json
{
  "action": "created",
  "video": {
    "id": "1a5f631f-d2cc-43b4-ad3b-8608d8b9df7d",
    "thumb_file": "https://some-provider-and-bucket/catalago-de-videos/some-uuid-hex-verbose/thumb/file.ext",
    "banner_file": "https://some-provider-and-bucket/catalago-de-videos/some-uuid-hex-verbose/banner/file.ext",
    "trailer_file": "https://some-provider-and-bucket/catalago-de-videos/some-uuid-hex-verbose/trailer/file.ext",
    "video_file": "https://some-provider-and-bucket/catalago-de-videos/some-uuid-hex-verbose/videos/file.ext"
  }
}
```

## Arquitetura utilizada

Utilizar a arquitetura hexagonal para que a regra de negócio, regra de aplicação e infraestrutura sejam independentes do framework utilizado.

A principio estaremos utilizando o django como framework primario para fazer o projeto funcionar.
Após sucessivas refatorações separando as devidas regras de negócio do framework poderemos iniciar a adição de outros frameworks

Ficando uma estrutura parecida com essa:

```shell
adapters/web
├── django
│   ├── apps
│   │   ├── ...../
│   ├── main
│   │   ├── wsgi.py
├── flask
│   ├── apps
│   │   ├── ...../
│   ├── main
│   │   ├── wsgi.py
├── fastapi
│   ├── apps
│   │   ├── ...../
│   ├── main
│   │   ├── wsgi.py
```

![clean architecture](https://guia.dev/assets/img/pictures/clean-architecture-min.jpg)

A pasta `src` conterá as regras de negócio e casos de uso utilizando python, interfaces (abc.ABC), repositorios, services como proposto pela arquitetura. Ficando idependente do framework

```shell

src
├── castmembers
│   ├── domain
│   │   └── entities.py
├── categories
│   ├── application
│   │   ├── use_cases
│   │   │   ├── create
│   │   │   │   ├── create.http
│   │   │   │   ├── create.py
│   │   │   │   ├── input.py
│   │   │   │   └── interface.py
│   │   │   ├── delete
│   │   │   ├── get
│   │   │   ├── search
│   │   │   └── update
│   ├── domain
│   │   ├── entities.py
│   │   ├── factories.py
│   │   ├── repositories.py
│   │   └── validators.py
├── core
│   ├── domain
│   │   ├── entities.py
│   │   ├── exceptions.py
│   │   ├── repositories.py
│   │   ├── unique_entity_id.py
│   │   ├── validators.py
│   │   └── value_objects.py
├── genres
│   ├── domain
│   │   └── entities.py
└── videos
    ├── domain
    │   └── entities.py
```

## Demo

![Demo com setup local](https://megustaviajar.sfo2.cdn.digitaloceanspaces.com/demo_setup_local.gif)

## Run Locally. Two alternatives

### Docker

Requisitos

- [x] Ter o docker e docker-compose instalado na maquina
- [ ] Customizar o arquivo `.devcontainer/gitconfig` para as suas necessidades

Serviços levantados

- [x] Redis
- [x] PostgreSQL
- [x] Celery
- [x] RabbitMQ
- [x] Django

```shell
❯ docker-compose up --build --force-recreate
❯ docker-compose exec catalog-svc zsh
```

### Virtualenv ou poetry

Requisitos

- [x] Python 3.10 instalado

Sugiro instalar o [asdf](http://asdf-vm.com/guide/getting-started.html#_1-install-dependencies)

```shell
❯ asdf plugin-add python
❯ asdf install python 3.10.4
```

- [x] Dependencias para o pacote Pillow

[dependencias externas](https://pillow.readthedocs.io/en/stable/installation.html#external-libraries)

- [x] Poetry instalado ou virtualenv

`python3 -m venv .venv` ou `poetry shell`

- [x] Postgres ou Postgis instalado.

Pode instalar direto no sistema operacional ou criar uma imagem docker como abaixo:

```shell
❯ dk run -itd --network thirdservices --name postgis -p 25432:5432 -e POSTGRES_USER=postgres -e POSTGRES_PASS=postgres kartoza/postgis
```

Com o postgres executando acesse o shell do banco de dados

```shell
❯ psql -h localhost -U postgres -p 25432 -W
```

Crie o banco de dados.

```shell
postgres=# CREATE DATABASE dj_catalogo_videos;
CREATE DATABASE
```

Crie um usuario

```shell
postgres=# CREATE USER catalogo_videos;
CREATE ROLE
```

Altere a senha

```shell
postgres=# alter user catalogo_videos with encrypted password 'teste123';
ALTER ROLE
```

De permissoes ao banco de dados

```shell
postgres=# grant all privileges on database dj_catalogo_videos to catalogo_videos;
GRANT
```

- [x] Redis instalado.

Pode instalar direto no sistema operacional ou criar uma imagem docker como abaixo:

```shell
❯ dk run -itd --network thirdservices --name redis -p 6379:6379 redis:alpine
```

- [x] RabbitMQ instalado.

Pode instalar direto no sistema operacional ou criar uma imagem docker como abaixo:

```shell
❯ docker run -d --name rabbitmq --net thirdservices --hostname rabbitmq-server -p 4369:4369 -p 25672:25672 -p 35197:35197 -p 5672:5672 -p 15672:15672 -e RABBITMQ_DEFAULT_USER=guest -e RABBITMQ_DEFAULT_PASS=guest rabbitmq:management-alpine
```

### Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`DJANGO_DEBUG`

`SECRET_KEY`

`POSTGRES_DB`

`POSTGRES_USER`

`POSTGRES_PASSWORD`

`POSTGRES_HOST`

`POSTGRES_PORT`

`CELERY_BROKER_URL`

`CELERY_RESULT_BACKEND`

`AMQP_URI`

`EXCHANGE`

`EXCHANGE_DLX`

`CATALOG_VIDEOS_DEAD`

`CATALOG_VIDEOS_DEAD_RK`

`CATALOG_VIDEOS`

`CATALOG_VIDEOS_RK`

Exemplo

```ini
❯ cat .env
DJANGO_DEBUG=on
SECRET_KEY=your-secret-key
POSTGRES_DB=dj_catalogo_videos
POSTGRES_USER=catalogo_videos
POSTGRES_PASSWORD=teste123
POSTGRES_HOST=127.0.0.1
POSTGRES_PORT=25432
CELERY_BROKER_URL=redis://localhost:6379
CELERY_RESULT_BACKEND=redis://localhost:6379
AMQP_URI=amqp://guest:guest@localhost/
EXCHANGE=catalog_videos
EXCHANGE_DLX=catalog_videos_dlx
CATALOG_VIDEOS_DEAD=catalog_videos_created_dead
CATALOG_VIDEOS_DEAD_RK=catalog_videos_created.dead
CATALOG_VIDEOS=catalog_videos_created
CATALOG_VIDEOS_RK=catalog_videos_created
```

### Migrations

Executar as migrations

```shell
❯ python manage.py migrate --settings=main.settings.dev
```

### Start server

Executar o servidor de desenvolvimento

```shell
❯ make run_dev

❯ python manage.py runserver 5000 --settings=main.settings.dev

```

### Celery

Necessário informar a variavel de ambiente `DJANGO_SETTINGS_MODULE`

```shell
DJANGO_SETTINGS_MODULE=main.settings.dev celery -A main.celery worker -l DEBUG
```

### RabbitMQ

Criar a Fila catalog_videos_created

![](https://megustaviajar.sfo2.cdn.digitaloceanspaces.com/queue_catalog_videos_created.png)

Atentar-se aos parametro:

- x-dead-letter-exchange: catalog_videos_dlx

- x-dead-letter-routing-key: catalog_videos_created.dead

Criar as Exchange Video Created e fazer um bind com a fila catalog_videos_created

![](https://megustaviajar.sfo2.cdn.digitaloceanspaces.com/exchange_catalog_videos.png)

Criar a Fila catalog_videos_created_dead

![](https://megustaviajar.sfo2.cdn.digitaloceanspaces.com/queue_catalog_videos_created_dead.png)

Sem parametros adicionais

Criar a Exchange catalog_videos_dlx e fazer um bind com a fila catalog_videos_created_dead

![](https://megustaviajar.sfo2.cdn.digitaloceanspaces.com/exchange_catalog_videos_dlx.png)

### Outros comandos

Gerar mensagens de tradução

```shell
❯ django-admin makemessages -l pt_BR
processing locale pt_BR

❯ django-admin compilemessages -l pt_BR

❯ django-admin makemessages -l es
processing locale es

❯ django-admin compilemessages -l es

❯ django-admin makemessages -l de
processing locale de

❯ django-admin compilemessages -l de

❯ python manage.py makemessages --all
❯ python manage.py compilemessages
```

## Running Tests

Pela configuração do pytest ele gera o coverage report automaticamente.

```shell
❯ make test
❯ pytest
❯ pytest tests/integration/categories/test_categories.py::test_list_the_categories
❯ pytest -k "unit"
❯ pytest -k "integration"
❯ pytest -k "webtest"
```

Gerar o report separadamente

```shell
❯ coverage report
❯ coverage html
```

Visualizar o coverage no browser

```shell
❯ cd htmlcov
❯ python3 -m http.server 9000
Serving HTTP on 0.0.0.0 port 9000 (http://0.0.0.0:9000/) ...
```

### API Reference

Com o servidor executando acesse a url `http://localhost:5000/api/schema/swagger-ui/#/` ou `http://localhost:5000/api/schema/redoc/`

## Screenshots

![Execução dos testes](https://megustaviajar.sfo2.cdn.digitaloceanspaces.com/admin-catalogo-executando-testes.gif)

![Coverage](https://megustaviajar.sfo2.cdn.digitaloceanspaces.com/admin-catalogo-coverage.gif)

![API reference](https://megustaviajar.sfo2.cdn.digitaloceanspaces.com/admin-catalogo-api-reference.gif)

## Roadmap

[Issues](https://github.com/lucassimon/fc-catalogo-de-videos/issues)

# Links e tutoriais

http://www.adamwester.me/blog/django-rest-framework-multi-language/

https://django-parler.readthedocs.io/en/stable/quickstart.html

https://djangostars.com/blog/django-pytest-testing/

https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/

https://bmaingret.github.io/blog/2021-11-15-Docker-and-Poetry

https://github.com/veryacademy/docker-mastery-with-django

https://testdriven.io/blog/django-celery-periodic-tasks/

https://testdriven.io/courses/django-celery/auto-reload/

https://github.com/thepylot/docker-django-redis-celery
