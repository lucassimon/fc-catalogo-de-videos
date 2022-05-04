# Third
import pytest

# Apps
from tests import factories


@pytest.mark.integration
@pytest.mark.django_db(reset_sequences=True)
def test_dunder_str():
    obj = factories.VideoFactory.create(title="Test Str")
    assert obj.__str__() == "Test Str"
