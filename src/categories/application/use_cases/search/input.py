"""
Input para criar uma categoria
"""
# Python
from typing import Optional

# Apps
from src.core.application.dto import SearchInput
from src.core.domain.repositories import Filter
from src.categories.domain.repositories import CategoryRepository


class SearchCategoryInput(SearchInput[str]):
    pass
