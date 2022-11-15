from datetime import datetime
from typing import Optional

import pytest

from src.categories.application.use_cases.output import CategoryOutputDTO
from src.categories.application.use_cases.get.output import GetCategoryOutput


@pytest.mark.unit
def test_output():
    expected = {
        "id": str,
        "title": str,
        "is_deleted": bool,
        "created_at": datetime,
        "description": Optional[str],
        "status": Optional[int],
    }

    assert CategoryOutputDTO.__annotations__ == expected


@pytest.mark.unit
def test_get_category_output_is_subclass():
    assert issubclass(GetCategoryOutput, CategoryOutputDTO) is True
