from typing import Optional


import pytest

from src.core.application.dto import SearchInput, Filter


@pytest.mark.unit
def test_input():
    expected = {
        "page": Optional[int],
        "per_page": Optional[int],
        "sort": Optional[str],
        "sort_direction": Optional[str],
        "filters": Optional[Filter],
    }

    assert SearchInput.__annotations__ == expected
