# Third
import pytest
from rest_framework.exceptions import NotFound
from django_extensions.db.models import ActivatorModel

# Apps
from apps.core import utils
from src.categories.domain import entities


@pytest.mark.unit
def test_check_is_inactive_or_deleted():
    """
    Check it is inactive or deleted
    """
    data = dict(title="some test", slug="some-test", is_deleted=False, status=ActivatorModel.ACTIVE_STATUS)
    category = entities.Category(**data)

    data = dict(title="some test", slug="some-test", status=ActivatorModel.INACTIVE_STATUS, is_deleted=True)
    category_inactive_and_deleted = entities.Category(**data)

    data = dict(title="some test", slug="some-test", status=ActivatorModel.INACTIVE_STATUS, is_deleted=False)
    category_inactive = entities.Category(**data)

    data = dict(title="some test", slug="some-test", is_deleted=True)
    category_deleted = entities.Category(**data)

    assert utils.check_is_inactive_or_deleted(category) == False
    assert utils.check_is_inactive_or_deleted(category_inactive_and_deleted) == True
    assert utils.check_is_inactive_or_deleted(category_inactive) == True
    assert utils.check_is_inactive_or_deleted(category_deleted) == True


@pytest.mark.unit
def test_raises_not_found_check_is_inactive():
    data = dict(title="some test", slug="some-test", status=ActivatorModel.INACTIVE_STATUS, is_deleted=False)
    category_inactive = entities.Category(**data)

    with pytest.raises(NotFound):
        utils.raises_not_found_when_inactive_or_deleted(category_inactive)


@pytest.mark.unit
def test_raises_not_found_check_is_deleted():
    data = dict(title="some test", slug="some-test", is_deleted=True)
    category_deleted = entities.Category(**data)

    with pytest.raises(NotFound):
        utils.raises_not_found_when_inactive_or_deleted(category_deleted)


@pytest.mark.unit
def test_get_items_by_model_and_ids_returns_none_list():
    """
    Returns an empty list
    """

    items = utils.get_items_by_model_and_ids([1, 2], "Model")

    assert items == []
