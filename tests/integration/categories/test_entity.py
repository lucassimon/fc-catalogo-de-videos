import pytest
from pydantic import ValidationError


from src.categories.domain import entities

@pytest.mark.integration
@pytest.mark.skip
def test_category_validates_title_as_required():
    with pytest.raises(ValidationError):
        entities.Category(title=None, slug="some")


@pytest.mark.integration
@pytest.mark.skip
def test_category_validates_title_with_less_4_characters():
    with pytest.raises(ValidationError):
        entities.Category(title='1234', slug="some")


@pytest.mark.integration
@pytest.mark.skip
def test_category_validates_slug_as_required():
    with pytest.raises(ValidationError):
        entities.Category(title="12345", slug=None)


@pytest.mark.integration
@pytest.mark.skip
def test_category_validates_slug_with_less_4_characters():
    with pytest.raises(ValidationError):
        entities.Category(title='12345', slug="1234")

@pytest.mark.integration
@pytest.mark.skip
def test_category_validates_status_different_enum():
    with pytest.raises(ValidationError):
        entities.Category(title='12345', slug="12345", status=99)

