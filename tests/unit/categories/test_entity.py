import pytest
from dataclasses import is_dataclass


from django_extensions.db.models import ActivatorModel

from apps.categories import entities
from apps.core.utils import uuidv4


@pytest.mark.unit
def test_category_is_a_dataclass():
    assert is_dataclass(entities.Category) is True


@pytest.mark.unit
def test_category_constructor_default_params():
    data = dict(
        title="some test",
        slug="some-test",
    )
    category = entities.Category(**data)
    assert category.title == data["title"]
    assert category.slug == data["slug"]


@pytest.mark.unit
def test_category_constructor():
    data = dict(
        title="some test",
        slug="some-test",
        description="some description",
        status=ActivatorModel.ACTIVE_STATUS,
        code=uuidv4(),
    )
    category = entities.Category(**data)

    assert category.title == data["title"]
    assert category.slug == data["slug"]
    assert category.description == data["description"]
    assert category.status == data["status"]
    assert category.code == data["code"]
