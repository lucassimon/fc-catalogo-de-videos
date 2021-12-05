import pytest


@pytest.mark.django_db
def test_dunder_str(cast_member_factory):
    obj = cast_member_factory.create(name="Test Str")
    assert obj.__str__() == "Test Str"
