"""
Listar categorias
"""


# Python
from dataclasses import asdict

# Apps
from src.core.application.dto import PaginationOutputMapper
from src.core.domain.repositories import SearchParams, SearchResult
from src.core.application.use_case import UseCase
from src.categories.domain.repositories import CategoryRepository
from src.categories.application.use_cases.output import CategoryOutputDTO, CategoryOutputMapper
from src.categories.application.use_cases.search.input import SearchCategoryInput
from src.categories.application.use_cases.search.output import SearchCategoryOutput


class SearchCategoriesUseCase(UseCase[SearchCategoryInput, SearchCategoryOutput]):
    """
    Classe para listar categorias
    """

    repo: CategoryRepository

    def __init__(self, repo: CategoryRepository) -> None:
        self.repo = repo

    def execute(self, input_params: SearchCategoryInput) -> SearchCategoryOutput:
        search_params = SearchParams(**asdict(input_params))
        result = self.repo.search(params=search_params)
        return self.__to_output(result=result)

    def __to_output(self, result: SearchResult):
        items = list(
            map(
                lambda category: CategoryOutputMapper.to_output(klass=CategoryOutputDTO, category=category),
                result.items,
            )
        )
        return PaginationOutputMapper.from_child(SearchCategoryOutput).to_output(items=items, result=result)
