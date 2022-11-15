"""
Retorna uma lista de categorias
"""

# Apps
from src.core.application.dto import PaginationOutput
from src.categories.application.use_cases.output import CategoryOutputDTO


class SearchCategoryOutput(PaginationOutput[CategoryOutputDTO, str]):
    pass
