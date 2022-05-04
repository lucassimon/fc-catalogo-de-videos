# Third
import pytest

# Apps
from tests import factories
from apps.genres import models


@pytest.mark.integration
@pytest.mark.django_db(reset_sequences=True)
def test_dunder_str():
    genre = factories.GenreFactory.create(title="Test Str")
    assert genre.__str__() == "Test Str"


@pytest.mark.integration
@pytest.mark.django_db(reset_sequences=True)
def test_dunder_str_on_genre_has_category():
    genre_title = "Test Str"
    genre = factories.GenreWithCategoryFactory.create(title=genre_title)
    category_title = genre.categories.first().title

    genre_has_category = models.GenreHasCategory.objects.first()

    assert genre_has_category.__str__() == f"{genre_title}_{category_title}"
