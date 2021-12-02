import pytest

from rest_framework.exceptions import NotFound
from django_extensions.db.models import ActivatorModel

from apps.core import utils


@pytest.mark.django_db
def test_check_is_inactive_or_deleted(
    category_factory, category_inactive, category_deleted
):
    category = category_factory.create()
    category_inactive_and_deleted = category_factory.create(
        status=ActivatorModel.INACTIVE_STATUS, is_deleted=True
    )

    assert utils.check_is_inactive_or_deleted(category) == False
    assert utils.check_is_inactive_or_deleted(category_inactive_and_deleted) == True
    assert utils.check_is_inactive_or_deleted(category_inactive) == True
    assert utils.check_is_inactive_or_deleted(category_deleted) == True


@pytest.mark.django_db
def test_check_is_inactive_or_deleted(category_inactive, category_deleted):

    with pytest.raises(NotFound):
        utils.raises_not_found_when_inactive_or_deleted(category_inactive)
        utils.raises_not_found_when_inactive_or_deleted(category_deleted)
