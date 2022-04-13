import pytest
from dataclasses import is_dataclass, FrozenInstanceError


from django_extensions.db.models import ActivatorModel

from src.categories.domain import entities


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
    )
    category = entities.Category(**data)

    assert category.title == data["title"]
    assert category.slug == data["slug"]
    assert category.description == data["description"]
    assert category.status == data["status"]


@pytest.mark.unit
def test_is_immutable():
    data = dict(
        title="some test",
        slug="some-test",
    )
    category = entities.Category(**data)
    with pytest.raises(FrozenInstanceError):
        category.title = 'set name'


@pytest.mark.unit
def test_category_set_some_attribute():
    data = dict(
        title="some test",
        slug="some-test",
        description="some description",
        status=ActivatorModel.ACTIVE_STATUS,
    )
    category = entities.Category(**data)
    category._set('title', 'new title')
    assert category.title == "new title"


@pytest.mark.unit
def test_category_activate():
    data = dict(
        title="some test",
        slug="some-test",
        description="some description",
        status=ActivatorModel.INACTIVE_STATUS,
    )
    category = entities.Category(**data)
    category.activate()
    assert category.status == ActivatorModel.ACTIVE_STATUS


@pytest.mark.unit
def test_category_deactivate():
    data = dict(
        title="some test",
        slug="some-test",
        description="some description",
        status=ActivatorModel.ACTIVE_STATUS,
    )
    category = entities.Category(**data)
    category.deactivate()
    assert category.status == ActivatorModel.INACTIVE_STATUS


@pytest.mark.unit
def test_category_update():
    data = dict(
        title="some test",
        slug="some-test",
        description="some description",
        status=ActivatorModel.INACTIVE_STATUS,
    )
    category = entities.Category(**data)

    new_data = dict(
        title="another title",
        slug="another-slug",
        description="another-description",
    )
    category.update(data=new_data)

    assert category.title == new_data["title"]
    assert category.slug == new_data["slug"]
    assert category.description == new_data["description"]
