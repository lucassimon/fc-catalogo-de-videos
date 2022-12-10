# Python
from typing import List

from django.core import exceptions as django_exceptions
from django.core.paginator import Paginator

# Third
from kernel_catalogo_videos.categories.domain.entities import Category as CategoryEntity
from kernel_catalogo_videos.core.domain.unique_entity_id import UniqueEntityId
from kernel_catalogo_videos.categories.domain.repositories import CategoryRepository

# Apps
from apps.core.exceptions import OperationDBErrorAPIException
from apps.categories.models import Category as CategoryModel
from apps.categories.mappers import CategoryModelMapper


class CategoryDjangoRepository(CategoryRepository):

    sortable_fields: List[str] = ['title', 'created_at']

    def insert(self, entity: CategoryEntity) -> None:
        model = CategoryModelMapper.to_model(entity)
        model.save()

    def find_by_id(self, entity_id: str | UniqueEntityId) -> CategoryEntity:
        id_str = str(entity_id)
        model = self._get(id_str)
        return CategoryModelMapper.to_entity(model)

    def find_all(self) -> List[CategoryEntity]:
        return [CategoryModelMapper.to_entity(model) for model in CategoryModel.objects.all()]

    def update(self, entity: CategoryEntity) -> None:
        model = self._get(entity.id)
        model.title = entity.title
        model.slug = entity.slug
        model.status = entity.status
        model.description = entity.description
        model.is_deleted = entity.is_deleted
        model.save()

    def delete(self, entity_id: str | UniqueEntityId) -> None:
        id_str = str(entity_id)
        model = self._get(id_str)
        model.delete()

    def _get(self, entity_id: str) -> CategoryModel:
        try:
            return CategoryModel.objects.get(pk=entity_id)
        except (CategoryModel.DoesNotExist, django_exceptions.ValidationError) as exc: # pylint: disable=no-member
            raise OperationDBErrorAPIException(
                exc=exc,
                code=404,
                operation="Get category",
                input_params={"id": entity_id},
            ) from exc
            # raise OperationDBErrorAPIException()

    def search(self, params: CategoryRepository.SearchParams) -> CategoryRepository.SearchResult:
        query = CategoryModel.objects.all()

        if params.filters:
            query = query.filter(name__icontains=params.filters)

        if params.sort and params.sort in self.sortable_fields:
            query = query.order_by(
                params.sort if params.sort_dir == 'asc' else f'-{params.sort}'
            )
        else:
            query = query.order_by('-created')

        paginator = Paginator(query, params.per_page)
        page_obj = paginator.page(params.page)

        return CategoryRepository.SearchResult(
            items=[CategoryModelMapper.to_entity(
                model) for model in page_obj.object_list],
            total=paginator.count,
            current_page=params.page,
            per_page=params.per_page,
            sort=params.sort,
            sort_direction=params.sort_direction,
            filters=params.filters
        )
