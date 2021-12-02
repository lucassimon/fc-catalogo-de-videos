# API de catalogos

## Executar o ambiente de desenvolvimento

```shell
❯ DJANGO_READ_DOT_ENV_FILE="on" python manage.py runserver --settings=main.settings.dev
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
November 30, 2021 - 23:41:11
Django version 3.2.6, using settings 'main.settings.dev'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
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
```

```shell
❯ coverage report
❯ coverage html
```

# Links e tutoriais

http://www.adamwester.me/blog/django-rest-framework-multi-language/

https://django-parler.readthedocs.io/en/stable/quickstart.html

https://djangostars.com/blog/django-pytest-testing/
