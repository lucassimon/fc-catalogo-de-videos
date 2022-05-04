"""
Define os repositories para a categoria
"""
# Python
import abc

# Apps
from src.core.domain.repositories import InMemoryRepository, RepositoryInterface

# Local
from .entities import Category


class CategoryRepository(RepositoryInterface[Category], abc.ABC):
    """
    Classe para tratar uma categoria
    """
    pass


class CategoryInMemoryRepository(CategoryRepository, InMemoryRepository[Category]):
    """
    Classe para tratar um repositorio em memória
    """
    pass
