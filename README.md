# API de catalogos

O Problema a ser resolvido:

Como administrador de uma plataforma de exibição de filmes, documentarios ou séries, quero poder administrar categorias, generos, elenco e os videos em uma pagina administrativa.

## Regras de negócio

Por ordem de prioridade

- [ ] O administrador pode criar, recuperar, listar, atualizar e deletar as categorias de um video

- [ ] O administrador pode criar, recuperar, listar, atualizar e deletar as generos de um video

- [ ] O administrador pode criar, recuperar, listar, atualizar e deletar um video

  - [ ] Ao criar um video uma categoria ou genero não podem estar deletadas ou inativas

  - [ ] Ao criar o administrador pode fazer upload 4 arquivos: uma thumbnail, uma imagem de capa, um trailler, o video completo

  - [ ] Ao deletar um video estes devem ser excluidos da cdn assim como suas variações. Ex: thumbnails_x_y.ext, videos_xyz_144p.ext, videos_xyz_240p.ext, videos_xyz_360p.ext ...

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

## Demo

TODO: Inserir um link para api e nextjs

## Run Locally

### Docker

Requisitos

- [x] Ter o docker instalado na maquina

Serviços levantados

- [x] Redis
- [x] PostgreSQL
- [x] Celery
- [x] Django

```shell
❯ docker-compose up --build --force-recreate
❯ docker-compose exec catalog-svc sh
```

### Virtualenv ou poetry

Requisitos

- [x] Python 3.10 instalado

Sugiro a instalar o [asdf](http://asdf-vm.com/guide/getting-started.html#_1-install-dependencies)

```shell
❯ asdf plugin-add python
❯ asdf install python 3.10.4
```

- [x] Poetry instalado ou virtualenv

- [x] Criar um virtualenv:

`python3 -m venv .venv`

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

❯ python manage.py runserver --settings=main.settings.dev

```

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

Com o servidor executando acesse a url `http://localhost:8000/api/schema/swagger-ui/#/` ou `http://localhost:8000/api/schema/redoc/`

## Screenshots

![Execução dos testes](https://megustaviajar.sfo2.cdn.digitaloceanspaces.com/admin-catalogo-executando-testes.gif)

![Coverage](https://megustaviajar.sfo2.cdn.digitaloceanspaces.com/admin-catalogo-coverage.gif)

![API reference](https://megustaviajar.sfo2.cdn.digitaloceanspaces.com/admin-catalogo-api-reference.gif)

## Roadmap

- Adicionar suporte ao black no precommit. Na versão 3.10 do python estava tendo problemas

- Adicionar suporte ao pylint / pylance

- Adicionar a ferramenta sonarcube no dockercompose

- Adicionar github actions e codebuilder como pipeline. Steps:

  1 - Lint,
  2 - pytest -k "unit",
  3 - pytest -k "integration",
  4 - pytest -k "unit"
  5 - build image
  6 - deploy image
  7 - deploy to kubenertes cluster

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
