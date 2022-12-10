# Third
from kernel_catalogo_videos.categories.domain.entities import Category as CategoryEntity
from kernel_catalogo_videos.core.domain.unique_entity_id import UniqueEntityId

# Apps
from apps.categories.models import Category as CategoryModel


class CategoryModelMapper:
    @staticmethod
    def to_entity(model: CategoryModel) -> CategoryEntity:
        return CategoryEntity(
            unique_entity_id=UniqueEntityId(str(model.id)),
            title=model.title,
            description=model.description,
            is_deleted=model.is_deleted,
            status=model.status,
            created_at=model.created,
        )

    @staticmethod
    def to_model(entity: CategoryEntity) -> CategoryModel:
        return CategoryModel(
            title=entity.title,
            slug=entity.slug,
            description=entity.description,
            status=entity.status,
            is_deleted=entity.is_deleted,
            created=entity.created_at,
        )
