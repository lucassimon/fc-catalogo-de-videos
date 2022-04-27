import abc

from src.core.domain.repositories import RepositoryInterface, InMemoryRepository
from .entities import Category


class CategoryRepository(RepositoryInterface[Category], abc.ABC):
    pass


class CategoryInMemoryRepository(CategoryRepository, InMemoryRepository[Category]):
    pass
