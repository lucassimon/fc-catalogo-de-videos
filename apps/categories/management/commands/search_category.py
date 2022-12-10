# Python
from typing import Any

from django.core.management.base import BaseCommand

# Third
from kernel_catalogo_videos.core.logging import make_logger
from kernel_catalogo_videos.categories.application import (
    SearchCategoryInput,
    SearchCategoryOutput,
    SearchCategoriesUseCase,
)

# Apps
from apps.categories.repositories import CategoryDjangoRepository

logger = make_logger(debug=True)


class Command(BaseCommand):
    help = 'List category'

    def add_arguments(self, parser):
        parser.add_argument('category_id', type=str, help='Category UUID')

    def handle(self, *args, **kwargs):
        # output = SearchCategoryCommand.run(args, pk=category_pk)
        pass


class SearchCategoryCommand:

    @staticmethod
    def run(params: dict[str, Any], *args, **kwargs: dict[str, Any]):
        input_params = SearchCategoryInput(**params)

        repo: CategoryDjangoRepository = CategoryDjangoRepository()
        use_case: SearchCategoriesUseCase = SearchCategoriesUseCase(repo=repo, logger=logger)
        output: SearchCategoryOutput = use_case.execute(input_params=input_params)

        return output
