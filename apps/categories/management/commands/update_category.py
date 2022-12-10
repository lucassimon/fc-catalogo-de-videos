# Python
from typing import Any, Mapping

from django.core.management.base import BaseCommand

# Third
from kernel_catalogo_videos.core.logging import make_logger
from kernel_catalogo_videos.categories.application import (
    UpdateCategoryInput,
    UpdateCategoryOutput,
    UpdateCategoryUseCase,
)

# Apps
from apps.core.exceptions import InvalidDataException
from apps.categories.serializers import CategorySerializer
from apps.categories.repositories import CategoryDjangoRepository

logger = make_logger(debug=True)


class Command(BaseCommand):
    help = 'Update category'

    def add_arguments(self, parser):
        parser.add_argument('category_id', type=str, help='Category UUID')
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

        UpdateCategoryCommand.run(payload=payload, *args, pk=kwargs["category_id"])



class UpdateCategoryCommand:
    @staticmethod
    def save_in_database(payload: Mapping[str, Any], *_, **kwargs: dict[str, Any]):
        if payload is None:
            raise InvalidDataException(
                exc=None,
                code=422,
                operation="Update category",
                payload=payload
            )

        try:
            repo: CategoryDjangoRepository = CategoryDjangoRepository()
            instance = repo.find_by_id(entity_id=kwargs["pk"])
            serializer = CategorySerializer(instance, data=payload, partial=False)
            serializer.is_valid(raise_exception=True)
            data = serializer.data
            validated_data = serializer.validated_data

            input_params = UpdateCategoryInput(
                **data
            )

            if "title" in validated_data:
                input_params.title = validated_data["title"]

            if "description" in validated_data:
                input_params.description = validated_data["description"]

            if "status" in validated_data:
                input_params.status = validated_data["status"]

            if "is_deleted" in validated_data:
                input_params.is_deleted = validated_data["is_deleted"]

            use_case: UpdateCategoryUseCase = UpdateCategoryUseCase(repo=repo, logger=logger)
            output: UpdateCategoryOutput = use_case.execute(input_params=input_params)
            return output

        except Exception as exc:
            raise exc

    @staticmethod
    def run(payload: Mapping[str, Any], *args, **kwargs: dict[str, Any]):
        output = UpdateCategoryCommand.save_in_database(payload, *args, **kwargs)

        return output
