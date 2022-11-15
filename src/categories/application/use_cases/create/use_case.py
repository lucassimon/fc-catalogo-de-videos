"""
Caso de uso para criar uma categoria
"""


# Apps
from src.core.application.use_case import UseCase
from src.categories.domain.entities import Category
from src.categories.domain.repositories import CategoryRepository
from src.categories.application.use_cases.output import CategoryOutputMapper
from src.categories.application.use_cases.create.input import CreateCategoryInput
from src.categories.application.use_cases.create.output import CreateCategoryOutput


class CreateCategoryUseCase(UseCase[CreateCategoryInput, CreateCategoryOutput]):
    """
    Classe para criar uma categoria
    """

    repo: CategoryRepository

    def __init__(self, repo: CategoryRepository) -> None:
        self.repo = repo

    def execute(self, input_params: CreateCategoryInput) -> CreateCategoryOutput:
        # pylint: disable=unexpected-keyword-arg
        category = Category(title=input_params.title, description=input_params.description, status=input_params.status)
        self.repo.insert(category)
        return self.__to_output(category=category)

    def __to_output(self, category: Category):
        # TODO: Utilizar o Output do create
        return CategoryOutputMapper.to_output(klass=CreateCategoryOutput, category=category)
