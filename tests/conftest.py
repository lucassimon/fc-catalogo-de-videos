import pytest

from pytest_factoryboy import register

from tests.factories.categories import CategoryFactory


register(CategoryFactory)
register(CategoryFactory, "category_inactive", status=0)
register(CategoryFactory, "category_deleted", is_deleted=True)


@pytest.fixture
def api_client():
    from rest_framework.test import APIClient

    return APIClient()
