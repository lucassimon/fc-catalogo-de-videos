import pytest
from dataclasses import is_dataclass, FrozenInstanceError


from django_extensions.db.models import ActivatorModel

from src.categories.domain import entities

import ipdb
from devtools import debug as ddebug

from src.core.domain.exceptions import EntityValidationException

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


@pytest.mark.unit
def test_category_title_is_invalid():
    data = dict(
        title=5,
        slug="some-test",
        description="some description",
        status=ActivatorModel.ACTIVE_STATUS,
    )

    with pytest.raises(EntityValidationException) as assert_error:
        entities.Category(**data)

    assert assert_error.value.error['title'] == ['Not a valid string.']


@pytest.mark.unit
def test_category_title_is_too_long():
    data = dict(
        title='a' * 256,
        slug="some-test",
        description="some description",
        status=ActivatorModel.ACTIVE_STATUS,
    )

    with pytest.raises(EntityValidationException) as assert_error:
        entities.Category(**data)

    assert assert_error.value.error['title'] == ['Ensure this field has no more than 255 characters.']



@pytest.mark.unit
def test_category_status_is_invalid():
    data = dict(
        title='some test',
        slug="some-test",
        description="some description",
        status=3,
    )

    with pytest.raises(EntityValidationException) as assert_error:
        entities.Category(**data)

    assert assert_error.value.error['status'] == ['"3" is not a valid choice.']


@pytest.mark.unit
def test_category_description_is_invalid():
    data = dict(
        title='some test',
        slug="some-test",
        description=5,
    )

    with pytest.raises(EntityValidationException) as assert_error:
        entities.Category(**data)

    assert assert_error.value.error['description'] == ['Not a valid string.']


@pytest.mark.unit
def test_category_is_deleted_is_invalid():
    data = dict(
        title='some test',
        slug="some-test",
        description='some description',
        is_deleted='1'
    )

    with pytest.raises(EntityValidationException) as assert_error:
        entities.Category(**data)

    assert assert_error.value.error['is_deleted'] == ['Must be a valid boolean.']
