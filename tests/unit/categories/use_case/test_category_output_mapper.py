from datetime import datetime


import pytest

from src.categories.application.use_cases.output import CategoryOutputDTO, CategoryOutputMapper
from src.categories.domain.entities import Category


@pytest.mark.unit
def test_category_output_mapper():
    created_at = datetime.now()
    # pylint: disable=unexpected-keyword-arg
    category = Category(title="test", description="some description", status=1, is_deleted=False, created_at=created_at)

    output = CategoryOutputMapper.to_output(klass=CategoryOutputDTO, category=category)

    assert output == CategoryOutputDTO(
        id=category.id,
        title=category.title,
        description=category.description,
        status=category.status,
        is_deleted=category.is_deleted,
        created_at=category.created_at,
    )
