from abc import ABC
import pytest

from dataclasses import dataclass, is_dataclass, FrozenInstanceError
from apps.core import value_objects

@dataclass(frozen=True)
class StubOneProp(value_objects.ValueObject):
    foo: str

@dataclass(frozen=True)
class StubTwoProp(value_objects.ValueObject):
    foo: str
    marco: str

@pytest.mark.unit
def test_value_object_is_a_dataclass():
    assert is_dataclass(value_objects.ValueObject) is True


@pytest.mark.unit
def test_value_object_is_a_abstract_class():
    assert isinstance(value_objects.ValueObject(), ABC)

@pytest.mark.unit
def test_init_prop():
    obj1 = StubOneProp(foo="bar")
    assert obj1.foo == "bar"

    obj2 = StubTwoProp(foo="bar", marco="polo")
    assert obj2.foo == "bar"
    assert obj2.marco == "polo"

@pytest.mark.unit
def test_dunder_str():
    obj1 = StubOneProp(foo="bar")
    assert obj1.__str__() == "bar"

    obj2 = StubTwoProp(foo="bar", marco="polo")
    assert obj2.__str__() == '{"foo": "bar", "marco": "polo"}'


@pytest.mark.unit
def test_is_immutable():
    obj = StubOneProp(foo="bar")
    with pytest.raises(FrozenInstanceError):
        obj.foo = 'set another id'

