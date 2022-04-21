import pytest

from tests import factories
from apps.core import utils


@pytest.mark.integration
@pytest.mark.django_db(reset_sequences=True)
def test_get_genres_by_ids():
    genres_created = factories.GenreFactory.create_batch(3)
    pks = [genres_created[0].pk, genres_created[1].pk]

    genres = utils.get_genres_by_ids(pks)
    expected_pks = genres.values_list("id", flat=True)

    for pk in pks:
        assert pk in expected_pks


@pytest.mark.integration
@pytest.mark.django_db(reset_sequences=True)
def test_get_categories_by_ids():
    categories_created = factories.CategoryFactory.create_batch(3)
    pks = [categories_created[0].pk, categories_created[1].pk]

    categories = utils.get_categories_by_ids(pks)
    expected_pks = categories.values_list("id", flat=True)

    for pk in pks:
        assert pk in expected_pks


@pytest.mark.integration
@pytest.mark.django_db(reset_sequences=True)
def test_get_items_by_model_and_ids_returns_categories_list():
    categories_created = factories.CategoryFactory.create_batch(3)
    pks = [categories_created[0].pk, categories_created[1].pk]

    items = utils.get_items_by_model_and_ids(pks, "Category")

    for pk in pks:
        assert pk in items.values_list("id", flat=True)

@pytest.mark.integration
@pytest.mark.django_db(reset_sequences=True)
def test_get_items_by_model_and_ids_returns_genres_list():
    genres_created = factories.GenreFactory.create_batch(3)
    pks = [genres_created[0].pk, genres_created[1].pk]

    items = utils.get_items_by_model_and_ids(pks, "Genre")

    for pk in pks:
        assert pk in items.values_list("id", flat=True)


@pytest.mark.integration
@pytest.mark.django_db(reset_sequences=True)
def test_check_all_items_are_available_returns_true():
    categories_created = factories.CategoryFactory.create_batch(3)
    pks = [categories_created[0].pk, categories_created[1].pk]

    expected = utils.check_all_items_are_available(pks, "Category")

    assert expected == True


@pytest.mark.integration
@pytest.mark.django_db(reset_sequences=True)
def test_check_all_items_are_available_raises_exception_when_is_deleted_is_true():
    category_deleted = factories.CategoryFactory.create(is_deleted=True)
    pks = [category_deleted.pk]

    with pytest.raises(Exception):
        utils.check_all_items_are_available(pks, "Category")

@pytest.mark.integration
@pytest.mark.django_db(reset_sequences=True)
def test_check_genres_are_in_categories():
    genre = factories.GenreWithCategoryFactory.create()
    categories_pks = genre.categories.all().values_list("pk", flat=True)

    exists = utils.check_genres_are_in_categories(genre.pk, categories_pks)

    assert exists == True

@pytest.mark.integration
@pytest.mark.django_db(reset_sequences=True)
def test_check_genres_are_in_categories_raises_exception():
    categories = factories.CategoryFactory.create_batch(3)
    genre = factories.GenreFactory.create()
    categories_pks = [categories[0].pk, categories[1].pk, categories[2].pk]

    with pytest.raises(Exception):
        utils.check_genres_are_in_categories(genre.pk, categories_pks)
