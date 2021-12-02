import pytest

from django_extensions.db.models import ActivatorModel

from apps.categories import models


@pytest.mark.django_db
def test_dunder_str(category_factory):
    category = category_factory.create(title="Test Str")
    assert category.__str__() == "Test Str"


@pytest.mark.django_db
def test_soft_deleted(category_factory):
    category = category_factory.create()
    category.soft_delete()

    assert category.is_deleted == True


@pytest.mark.django_db
def test_restore_the_deleted_instance(category_factory):
    category = category_factory.create()
    category.soft_delete()

    category.restore()

    assert category.is_deleted == False
    assert category.deleted_at is None


@pytest.mark.django_db
def test_queryset_inactive(category_factory):
    category_factory.create_batch(2, status=ActivatorModel.INACTIVE_STATUS)
    categories = models.Category.objects.inactive()

    assert categories.count() == 2


@pytest.mark.django_db
def test_queryset_deleted(category_factory):
    category_factory.create_batch(2, is_deleted=True)
    categories = models.Category.objects.deleted()

    assert categories.count() == 2


@pytest.mark.django_db
def test_queryset_undeleted(category_factory):
    category_factory.create_batch(2)
    categories = models.Category.objects.undeleted()

    assert categories.count() == 2
