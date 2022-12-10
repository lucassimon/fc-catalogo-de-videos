from django.core.management.base import BaseCommand

# Third
from kernel_catalogo_videos.core.logging import make_logger
from kernel_catalogo_videos.categories.application import GetCategoryInput, GetCategoryOutput, GetCategoryUseCase

# Apps
from apps.categories.repositories import CategoryDjangoRepository

logger = make_logger(debug=True)


class Command(BaseCommand):
    help = 'Retrieve category'

    def add_arguments(self, parser):
        parser.add_argument('category_id', type=str, help='Category UUID')

    def handle(self, *args, **kwargs):
        categories_ids = kwargs['category_id']

        for category_pk in categories_ids:
            RetrieveCategoryCommand.run(args, pk=category_pk)



class RetrieveCategoryCommand:

    @staticmethod
    def run(*args, **kwargs: dict):
        repo: CategoryDjangoRepository = CategoryDjangoRepository()
        repo.find_by_id(entity_id=kwargs["pk"])

        input_params = GetCategoryInput(id=kwargs["pk"])

        use_case: GetCategoryUseCase = GetCategoryUseCase(repo=repo, logger=logger)
        output: GetCategoryOutput = use_case.execute(input_params=input_params)

        return output
