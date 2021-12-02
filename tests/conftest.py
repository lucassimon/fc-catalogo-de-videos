import pytest

from pytest_factoryboy import register
from django_extensions.db.models import ActivatorModel


from tests.factories.categories import CategoryFactory


register(CategoryFactory)
register(CategoryFactory, "category_inactive", status=ActivatorModel.INACTIVE_STATUS)
register(CategoryFactory, "category_deleted", is_deleted=True)


@pytest.fixture
def api_client():
    from rest_framework.test import APIClient

    return APIClient()
