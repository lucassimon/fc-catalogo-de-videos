# Python
from typing import Any, Mapping

from django.core.management.base import BaseCommand

# Third
from kernel_catalogo_videos.core.logging import make_logger
from kernel_catalogo_videos.categories.application import (
    CreateCategoryInput,
    CreateCategoryOutput,
    CreateCategoryUseCase,
)

# Apps
from apps.core.exceptions import InvalidDataException
from apps.categories.serializers import CategorySerializer
from apps.categories.repositories import CategoryDjangoRepository

logger = make_logger(debug=True)


class Command(BaseCommand):
    help = 'Create category'

    def add_arguments(self, parser):
        parser.add_argument('title', '--title', type=str, help='Define the title')
        parser.add_argument('description', '--description', type=str, help='Define the description')
        parser.add_argument('status', type=int, help='Indicates active or inactive')
        parser.add_argument('deleted', type=bool, help='Indicates is is deleted')

    def handle(self, *args, **kwargs):
        payload = {
            "title": kwargs['title'],
            "description": kwargs['description'],
            "status": kwargs['status'],
            "is_deleted": kwargs['is_deleted'],
        }

        CreateCategoryCommand.run(payload=payload, *args, **kwargs)



class CreateCategoryCommand:
    @staticmethod
    def save_in_database(payload: Mapping[str, Any], *_, **kwargs: dict[str, Any]):
        if payload is None:
            raise InvalidDataException(
                exc=None,
                code=422,
                operation="Create category",
                payload=payload
            )

        try:
            repo: CategoryDjangoRepository = CategoryDjangoRepository()
            serializer = CategorySerializer(data=payload)
            serializer.is_valid(raise_exception=True)
            validated_data = serializer.validated_data

            input_params = CreateCategoryInput(
                **validated_data
            )

            use_case: CreateCategoryUseCase = CreateCategoryUseCase(repo=repo, logger=logger)
            output: CreateCategoryOutput = use_case.execute(input_params=input_params)
            return output

        except Exception as exc:
            raise exc

    @staticmethod
    def run(payload: Mapping[str, Any], *args, **kwargs: dict[str, Any]):
        output = CreateCategoryCommand.save_in_database(payload, *args, **kwargs)

        return output
