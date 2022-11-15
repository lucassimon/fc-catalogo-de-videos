"""
Define a entidade de Categoria
"""
# Python
from typing import Any, Dict, Optional
from datetime import datetime
from dataclasses import field, dataclass

# Third
from django_extensions.db.models import ActivatorModel

# Apps
from apps.core.utils import now
from src.core.domain.entities import Entity
from src.core.domain.exceptions import EntityValidationException
from apps.categories.serializers import CategorySerializer
from src.categories.domain.factories import CategoryValidatorFactory


@dataclass(kw_only=True, frozen=True, slots=True)
class Category(Entity):
    """
    Representa a entidade categoria e seus dados
    """

    title: str
    slug: Optional[str] = ""
    description: Optional[str] = ""
    status: Optional[int] = ActivatorModel.ACTIVE_STATUS
    is_deleted: bool = False
    created_at: Optional[datetime] = field(default_factory=lambda: now())

    def __post_init__(self):
        self.validate()

    def update(self, data: Dict[str, Any]):
        """
        Atualiza os dados internos da entidade
        """
        for field_name, value in data.items():
            self._set(field_name, value)

        self.validate()

    def _set(self, field_name, value):
        object.__setattr__(self, field_name, value)

        return self

    def activate(self):
        """
        Seta o atributo status como ativo
        """
        self._set("status", ActivatorModel.ACTIVE_STATUS)

    def deactivate(self):
        """
        Seta o atributo status como inativo
        """
        self._set("status", ActivatorModel.INACTIVE_STATUS)

    def validate(self):
        """
        Instancia um validador e executa o metodo validate
        """
        validator = CategoryValidatorFactory.create()
        is_valid = validator.check(serializer_class=CategorySerializer, data=self.to_dict())
        if not is_valid:
            raise EntityValidationException(validator.errors)
