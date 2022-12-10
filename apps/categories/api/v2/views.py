# Python
from http import HTTPStatus
from dataclasses import asdict

# Third
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from kernel_catalogo_videos.core.messages import Messages

# Apps
from apps.categories.management.commands.create_category import CreateCategoryCommand
from apps.categories.management.commands.delete_category import DeleteCategoryCommand
from apps.categories.management.commands.search_category import SearchCategoryCommand
from apps.categories.management.commands.update_category import UpdateCategoryCommand
from apps.categories.management.commands.retrieve_category import RetrieveCategoryCommand


class ListCreateCategoriesView(ListCreateAPIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        params = request.query_params.dict()
        output = SearchCategoryCommand.run(params, *args, **kwargs)

        return Response({
            "resouce": "categories",
            "message": Messages.RESOURCE_FETCHED_PAGINATED.value.format("categorias"),
            "data":asdict(output),
            "status": HTTPStatus.MULTIPLE_CHOICES
        }, status=HTTPStatus.MULTIPLE_CHOICES)

    def post(self, request, *args, **kwargs):
        payload = request.data or None
        output = CreateCategoryCommand.run(payload, *args, **kwargs)
        return Response({
            "resouce": "categories",
            "message": Messages.RESOURCE_CREATED.value.format("categoria"),
            "data":asdict(output),
            "status": HTTPStatus.CREATED
        }, status=HTTPStatus.CREATED)


class CategoryView(RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        output = RetrieveCategoryCommand.run(*args, **kwargs)

        return Response({
            "resouce": "categories",
            "message": Messages.RESOURCE_FETCHED.value.format("categoria"),
            "data":asdict(output),
            "status": HTTPStatus.FOUND
        }, status=HTTPStatus.FOUND)

    def update(self, request, *args, **kwargs):
        payload = request.data or None
        output = UpdateCategoryCommand.run(payload, *args, **kwargs)

        return Response({
            "resouce": "categories",
            "message": Messages.RESOURCE_UPDATED.value.format("categoria"),
            "data":asdict(output),
            "status": HTTPStatus.OK
        }, status=HTTPStatus.OK)

    def delete(self, request, *args, **kwargs):
        DeleteCategoryCommand.run(*args, **kwargs)

        return Response(status=HTTPStatus.NO_CONTENT)
