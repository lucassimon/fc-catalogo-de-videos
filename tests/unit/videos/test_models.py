import pytest


@pytest.mark.django_db
def test_dunder_str(video_factory):
    obj = video_factory.create(title="Test Str")
    assert obj.__str__() == "Test Str"
