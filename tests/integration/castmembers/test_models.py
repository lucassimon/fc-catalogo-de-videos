import pytest
from tests.factories import cast_members as factories

@pytest.mark.integration
@pytest.mark.django_db(reset_sequences=True)
def test_dunder_str():
    obj = factories.CastMemberFactory(name="Test Str")
    assert obj.__str__() == "Test Str"
