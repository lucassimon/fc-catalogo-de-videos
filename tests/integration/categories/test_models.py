import pytest

from django_extensions.db.models import ActivatorModel


from tests.factories import categories as factories
from apps.categories import models

@pytest.mark.integration
@pytest.mark.django_db(reset_sequences=True)
def test_dunder_str():
    category = factories.CategoryFactory.create(title="Test Str")
    assert category.__str__() == "Test Str"

@pytest.mark.integration
@pytest.mark.django_db(reset_sequences=True)
def test_soft_deleted():
    category = factories.CategoryFactory.create()
    category.soft_delete()

    assert category.is_deleted == True

@pytest.mark.integration
@pytest.mark.django_db(reset_sequences=True)
def test_restore_the_deleted_instance():
    category = factories.CategoryFactory.create()
    category.soft_delete()

    category.restore()

    assert category.is_deleted == False
    assert category.deleted_at is None

@pytest.mark.integration
@pytest.mark.django_db(reset_sequences=True)
def test_queryset_inactive():
    factories.CategoryFactory.create_batch(2, status=ActivatorModel.INACTIVE_STATUS)
    categories = models.Category.objects.inactive()

    assert categories.count() == 2

@pytest.mark.integration
@pytest.mark.django_db(reset_sequences=True)
def test_queryset_deleted():
    factories.CategoryFactory.create_batch(2, is_deleted=True)
    categories = models.Category.objects.deleted()

    assert categories.count() == 2

@pytest.mark.integration
@pytest.mark.django_db(reset_sequences=True)
def test_queryset_undeleted():
    factories.CategoryFactory.create_batch(2)
    categories = models.Category.objects.undeleted()

    assert categories.count() == 2
