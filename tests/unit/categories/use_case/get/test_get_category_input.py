import pytest

from src.categories.application.use_cases.get.input import GetCategoryInput


@pytest.mark.unit
def test_input():
    expected = {"id": str}

    assert GetCategoryInput.__annotations__ == expected
