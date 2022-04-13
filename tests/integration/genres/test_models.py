import pytest

from apps.genres import models

@pytest.mark.integration
@pytest.mark.django_db
def test_dunder_str(genre_factory):
    genre = genre_factory.create(title="Test Str")
    assert genre.__str__() == "Test Str"


@pytest.mark.integration
@pytest.mark.django_db
def test_dunder_str_on_genre_has_category(genre_with_category_factory):
    genre_title = "Test Str"
    genre = genre_with_category_factory.create(title=genre_title)
    category_title = genre.categories.first().title

    genre_has_category = models.GenreHasCategory.objects.first()

    assert genre_has_category.__str__() == f"{genre_title}_{category_title}"
