# Third
import pytest
from devtools import debug as ddebug
from rest_framework import serializers

# Apps
from src.core.domain import validators


class StubSerializer(serializers.Serializer):
    name = serializers.CharField()
    price = serializers.IntegerField()


@pytest.mark.integration
def test_drf_validator_with_error():
    validator = validators.DRFValidator()
    serializer = StubSerializer(data={})
    is_valid = validator.validate(validator=serializer)

    assert is_valid is False
    assert validator.errors == {"name": ["This field is required."], "price": ["This field is required."]}


@pytest.mark.integration
def test_drf_validator_with_validated_data():
    validator = validators.DRFValidator()
    serializer = StubSerializer(data={"name": "foo", "price": 5})
    is_valid = validator.validate(validator=serializer)

    assert is_valid is True
    assert validator.validated_data == {"name": "foo", "price": 5}
