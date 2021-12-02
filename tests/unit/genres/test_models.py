import pytest


@pytest.mark.django_db
def test_dunder_str(genre_factory):
    genre = genre_factory.create(title="Test Str")
    assert genre.__str__() == "Test Str"
