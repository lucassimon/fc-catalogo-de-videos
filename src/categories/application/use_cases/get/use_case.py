"""
Buscar uma  categoria
"""


# Apps
from src.core.application.use_case import UseCase
from src.categories.domain.entities import Category
from src.categories.domain.repositories import CategoryRepository
from src.categories.application.use_cases.output import CategoryOutputMapper
from src.categories.application.use_cases.get.input import GetCategoryInput
from src.categories.application.use_cases.get.output import GetCategoryOutput


class GetCategoryUseCase(UseCase[GetCategoryInput, GetCategoryOutput]):
    """
    Classe para criar uma categoria
    """

    repo: CategoryRepository

    def __init__(self, repo: CategoryRepository) -> None:
        self.repo = repo

    def execute(self, input_params: GetCategoryInput) -> GetCategoryOutput:
        category = self.repo.find_by_id(input_params.id)
        return self.__to_output(category=category)

    def __to_output(self, category: Category):
        # TODO: Utilizar o Output do get
        return CategoryOutputMapper.to_output(klass=GetCategoryOutput, category=category)
