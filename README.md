# API de catalogos

## Docker

```shell
❯ docker-compose up --build --force-recreate
❯ docker-compose exec catalog-svc sh
```

## Executar o ambiente de desenvolvimento

```shell
❯ make run_dev

❯ python manage.py runserver --settings=main.settings.dev

```

## Gerar mensagens de tradução

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

```

ou

```shell
❯ python manage.py makemessages --all
❯ python manage.py compilemessages
```

## Executar testes

Comandos disponíveis

```shell
❯ make test
❯ pytest
❯ pytest tests/integration/categories/test_categories.py::test_list_the_categories
❯ pytest -k "webtest"
❯ pytest -k "integration"
❯ pytest -k "unit"
```

```shell
❯ coverage report
❯ coverage html
```

# Links e tutoriais

http://www.adamwester.me/blog/django-rest-framework-multi-language/

https://django-parler.readthedocs.io/en/stable/quickstart.html

https://djangostars.com/blog/django-pytest-testing/

https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/
