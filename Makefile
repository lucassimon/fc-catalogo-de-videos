GIT_CURRENT_BRANCH := ${shell git symbolic-ref --short HEAD}

.PHONY: help clean test clean-build

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
	@rm -rf htmlcov/
	@rm -f .coverage
	@rm -f .coverage.*
	@rm -rf .cache/
	@rm -f coverage.xml
	@rm -f *.cover
	@rm -rf testresults
	@rm -rf .pytest_cache/


clean-build:
	rm --force --recursive build/
	rm --force --recursive dist/
	rm --force --recursive *.egg-info

.PHONY: lint
lint:
	@flake8

.PHONY: black
black:
	@black

.PHONY: isort
isort:
	@isort


test:
	@python manage.py compilemessages
	@pytest -s --verbose --cov=apps tests/

runserver:
	DJANGO_READ_DOT_ENV_FILE="on" python manage.py runserver --settings=main.settings.dev
