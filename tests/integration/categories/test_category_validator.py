# Third
import pytest

# Apps
from apps.categories.serializers import CategorySerializer
from src.categories.domain.validators import CategoryValidator


@pytest.mark.integration
def test_category_validator_with_data():
    validator = CategoryValidator()
    serializer_class = CategorySerializer
    data = dict(title='some-title')
    is_valid = validator.validate(serializer_class=serializer_class, data=data)
    assert is_valid is True
    assert validator.validated_data == {'title': 'some-title'}


@pytest.mark.integration
def test_category_validator_with_title_is_blank():
    validator = CategoryValidator()
    serializer_class = CategorySerializer
    data = dict(title='')
    is_valid = validator.validate(serializer_class=serializer_class, data=data)
    assert is_valid is False
    assert validator.errors == {'title': ['This field may not be blank.']}


@pytest.mark.integration
def test_category_validator_with_none_data():
    validator = CategoryValidator()
    serializer_class = CategorySerializer
    is_valid = validator.validate(serializer_class=serializer_class, data=None)
    assert is_valid is False
    assert validator.errors == {'title':  ['This field is required.']}


@pytest.mark.integration
def test_category_validator_with_empty_data():
    validator = CategoryValidator()
    serializer_class = CategorySerializer
    is_valid = validator.validate(serializer_class=serializer_class, data={})
    assert is_valid is False
    assert validator.errors == {'title':  ['This field is required.']}


@pytest.mark.integration
def test_category_validator_with_title_is_a_number():
    validator = CategoryValidator()
    serializer_class = CategorySerializer
    data = dict(title=5555)
    is_valid = validator.validate(serializer_class=serializer_class, data=data)
    assert is_valid is False
    assert validator.errors == {'title':  ['Not a valid string.']}


@pytest.mark.integration
def test_category_validator_with_title_has_more_than_255_chars():
    validator = CategoryValidator()
    serializer_class = CategorySerializer
    data = dict(title='a' * 256)
    is_valid = validator.validate(serializer_class=serializer_class, data=data)
    assert is_valid is False
    assert validator.errors == {'title':  ['Ensure this field has no more than 255 characters.']}


@pytest.mark.integration
def test_category_validator_with_description_is_a_number():
    validator = CategoryValidator()
    serializer_class = CategorySerializer
    data = dict(title='a', description=5)
    is_valid = validator.validate(serializer_class=serializer_class, data=data)
    assert is_valid is False
    assert validator.errors == {'description':  ['Not a valid string.']}


@pytest.mark.integration
def test_category_validator_with_description_has_more_than_255_chars():
    validator = CategoryValidator()
    serializer_class = CategorySerializer
    data = dict(title='a', description= 'a' * 256)
    is_valid = validator.validate(serializer_class=serializer_class, data=data)
    assert is_valid is False
    assert validator.errors == {'description':  ['Ensure this field has no more than 255 characters.']}


@pytest.mark.integration
def test_category_validator_with_is_deleted_is_zero():
    validator = CategoryValidator()
    serializer_class = CategorySerializer
    data = dict(title='a', description= 'a', is_deleted=0)
    is_valid = validator.validate(serializer_class=serializer_class, data=data)
    assert is_valid is False
    assert validator.errors == {'is_deleted':  ['Must be a valid boolean.']}
