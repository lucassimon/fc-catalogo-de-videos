# Python
import abc

# Apps
from src.core.domain.repositories import InMemoryRepository, RepositoryInterface

# Local
from .entities import Category


class CategoryRepository(RepositoryInterface[Category], abc.ABC):
    pass


class CategoryInMemoryRepository(CategoryRepository, InMemoryRepository[Category]):
    pass
