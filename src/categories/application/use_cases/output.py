"""
Output retornando os dados de uma categoria
"""

# Python
from typing import Optional
from datetime import datetime
from dataclasses import dataclass

# Apps
from src.categories.domain.entities import Category


@dataclass(slots=True, frozen=True)
class CategoryOutputDTO:
    id: str
    title: str
    is_deleted: bool
    created_at: datetime
    description: Optional[str] = None
    status: Optional[int] = 1


class CategoryOutputMapper:
    @staticmethod
    def to_output(klass, category: Category) -> CategoryOutputDTO:
        return klass(
            id=category.id,
            title=category.title,
            description=category.description,
            status=category.status,
            is_deleted=category.is_deleted,
            created_at=category.created_at,
        )
