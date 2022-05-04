# Python
from unittest.mock import PropertyMock, patch

# Third
import pytest
from rest_framework import serializers

# Apps
from src.core.domain import validators


@pytest.mark.unit
@patch.object(serializers.Serializer, 'is_valid', return_value=True)
@patch.object(serializers.Serializer, 'validated_data', return_value={'field': 'foo bar'}, new_callable=PropertyMock)
def test_when_validated_data_is_setted(mocked_validated_data, mocked_is_valid):

    validator = validators.DRFValidator()
    is_valid = validator.validate(serializers.Serializer())
    mocked_is_valid.assert_called_once()
    mocked_validated_data.assert_called_once()
    assert is_valid is True
    assert validator.validated_data == {'field': 'foo bar'}


@pytest.mark.unit
@patch.object(serializers.Serializer, 'is_valid', return_value=False)
@patch.object(serializers.Serializer, 'errors', return_value={'field': ['some error']}, new_callable=PropertyMock)
def test_when_errors_is_setted(mocked_errors, mocked_is_valid):

    validator = validators.DRFValidator()
    is_valid = validator.validate(serializers.Serializer())
    mocked_is_valid.assert_called_once()
    mocked_errors.assert_called_once()
    assert is_valid is False
    assert validator.errors == {'field': ['some error']}
