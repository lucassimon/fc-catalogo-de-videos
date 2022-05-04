# Third
import ipdb
import pytest
from devtools import debug as ddebug
from rest_framework.serializers import Serializer, ErrorDetail

# Apps
from apps.core import fields


class StubStrictCharFieldSerializer(Serializer):
    name = fields.StrictCharField()


class StubStrictCharFieldWithAllowNullSerializer(Serializer):
    name = fields.StrictCharField(required=False, allow_null=True)


class StubStrictBooleanFieldSerializer(Serializer):
    is_active = fields.StrictBooleanField()


class StubStrictBooleanFieldWithAllowNullSerializer(Serializer):
    is_active = fields.StrictBooleanField(required=False, allow_null=True)



@pytest.mark.integration
def test_strict_char_field_when_data_is_valid():
    serializer = StubStrictCharFieldWithAllowNullSerializer(data={ "name": 'some name' })
    is_valid = serializer.is_valid()

    assert is_valid is True


@pytest.mark.integration
def test_strict_char_field_when_data_is_an_integer():
    serializer = StubStrictCharFieldSerializer(data={ "name": 1 })
    serializer.is_valid()

    assert serializer.errors == {'name':  [ErrorDetail(string='Not a valid string.', code='invalid')]}


@pytest.mark.integration
def test_strict_char_field_when_data_is_a_boolean():
    serializer = StubStrictCharFieldSerializer(data={ "name": True })
    serializer.is_valid()

    assert serializer.errors == {'name':  [ErrorDetail(string='Not a valid string.', code='invalid')]}


@pytest.mark.integration
def test_strict_char_field_when_data_accepts_none():
    serializer = StubStrictCharFieldWithAllowNullSerializer(data={ "name": None })
    is_valid = serializer.is_valid()

    assert is_valid is True


@pytest.mark.integration
def test_strict_boolean_field_when_data_is_active_is_one():
    serializer = StubStrictBooleanFieldSerializer(data={ "is_active": 1 })
    serializer.is_valid()

    assert serializer.errors == {'is_active':  [ErrorDetail(string='Must be a valid boolean.', code='invalid')]}


@pytest.mark.integration
def test_strict_boolean_field_when_data_is_active_is_zero():
    serializer = StubStrictBooleanFieldSerializer(data={ "is_active": 0 })
    serializer.is_valid()

    assert serializer.errors == {'is_active':  [ErrorDetail(string='Must be a valid boolean.', code='invalid')]}



@pytest.mark.integration
def test_strict_boolean_field_when_data_is_active_is_true_as_string():
    serializer = StubStrictBooleanFieldSerializer(data={ "is_active": 'true' })
    serializer.is_valid()

    assert serializer.errors == {'is_active':  [ErrorDetail(string='Must be a valid boolean.', code='invalid')]}


@pytest.mark.integration
def test_strict_boolean_field_when_data_is_active_is_false_as_string():
    serializer = StubStrictBooleanFieldSerializer(data={ "is_active": 'false' })
    serializer.is_valid()

    assert serializer.errors == {'is_active':  [ErrorDetail(string='Must be a valid boolean.', code='invalid')]}


@pytest.mark.integration
def test_strict_boolean_field_when_data_not_accepts_none():
    serializer = StubStrictBooleanFieldSerializer(data={ "is_active": None })
    serializer.is_valid()

    assert serializer.errors == {'is_active':  [ErrorDetail(string='This field may not be null.', code='null')]}



@pytest.mark.integration
def test_strict_boolean_field_when_data_accepts_none():
    serializer = StubStrictBooleanFieldWithAllowNullSerializer(data={ "is_active": None })
    is_valid = serializer.is_valid()

    assert is_valid is True


@pytest.mark.integration
def test_strict_boolean_field_when_data_is_active_is_true_as_bool():
    serializer = StubStrictBooleanFieldWithAllowNullSerializer(data={ "is_active": True })
    is_valid = serializer.is_valid()

    assert is_valid is True


@pytest.mark.integration
def test_strict_boolean_field_when_data_is_active_is_false_as_bool():
    serializer = StubStrictBooleanFieldWithAllowNullSerializer(data={ "is_active": False })
    is_valid = serializer.is_valid()

    assert is_valid is True
