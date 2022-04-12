GIT_CURRENT_BRANCH := ${shell git symbolic-ref --short HEAD}
FLAKE8_FLAGS = --ignore=W503,E501
ISORT_FLAGS = --profile=black --lines-after-import=2

.PHONY: help clean test clean-build lint lint_black lint_isort black isort formatter run_dev migrations migrate makemessages coverage show_urls

.DEFAULT: help

help:
	@echo "make clean:"
	@echo "       Removes all pyc, pyo and __pycache__"
	@echo ""
	@echo "make clean-build:"
	@echo "       Clear all build directories"
	@echo ""
	@echo "make test:"
	@echo "       Run tests with coverage, lint, and clean commands"
	@echo ""


clean:
	find . -name '*.pyc' -exec rm --force {} +
	find . -name '*.pyo' -exec rm --force {} +
	find . | grep -E "__pycache__|.pytest_cache|.pyc|.DS_Store$$" | xargs rm -rf
	@rm -rf build/
	@rm -rf dist/
	@rm -f *.egg
	@rm -f *.eggs
	@rm -rf *.egg-info/
	@coverage erase || exit 1
	@rm -rf htmlcov/
	@rm -f .coverage
	@rm -f .coverage.*
	@rm -rf .cache/
	@rm -f coverage.xml
	@rm -f *.cover
	@rm -rf testresults
	@rm -rf .pytest_cache/


clean-build: clean
	rm --force --recursive build/
	rm --force --recursive dist/
	rm --force --recursive *.egg-info

lint:
	@flake8 ${FLAKE8_FLAGS} .

lint_black:
	@black --check apps/

lint_isort:
	@isort ${ISORT_FLAGS} --check apps/

## @ formatacao
black:
	@black apps/

isort:
	@isort ${ISORT_FLAGS} apps/

formatter: isort black

run_dev:
	@python manage.py runserver --settings=main.settings.dev

migrations:
	@python manage.py makemigrations --settings=main.settings.dev

migrate:
	@python manage.py migrate --settings=main.settings.dev

messages:
	@python manage.py makemessages --all

compilemessages:
	@python manage.py compilemessages

coverage:
	@coverage html

test: clean-build
	@pytest -s --verbose --cov=apps tests/

show_urls:
	@python manage.py show_urls --settings=main.settings.dev
