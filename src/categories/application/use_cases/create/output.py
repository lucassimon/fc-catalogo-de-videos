"""
Input para criar uma categoria
"""

# Python
from dataclasses import dataclass

# Apps
from src.categories.application.use_cases.output import CategoryOutputDTO


@dataclass(slots=True, frozen=True)
class CreateCategoryOutput(CategoryOutputDTO):
    pass
