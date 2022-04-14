import pytest

from src.categories.domain.validators import CategoryValidator
from apps.categories.serializers import CategorySerializer


@pytest.mark.integration
def test_category_validator_with_data():
    validator = CategoryValidator()
    serializer_class = CategorySerializer
    data = dict(title='some-title')
    is_valid = validator.validate(serializer_class=serializer_class, data=data)
    assert is_valid is True
    assert validator.validated_data == {'title': 'some-title'}


@pytest.mark.integration
def test_category_validator_with_title_error():
    validator = CategoryValidator()
    serializer_class = CategorySerializer
    data = dict(title='')
    is_valid = validator.validate(serializer_class=serializer_class, data=data)
    assert is_valid is False
    assert validator.errors == {'title': ['This field may not be blank.']}
