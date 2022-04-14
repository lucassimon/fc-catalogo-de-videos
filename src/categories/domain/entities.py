# Python
from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional, Dict, Any


# Third
from django_extensions.db.models import ActivatorModel

from enum import IntEnum
# Apps
from apps.core.utils import now
from apps.categories.serializers import CategorySerializer
from src.categories.domain.factories import CategoryValidatorFactory
from src.core.domain.entities import Entity

class StatusEnum(IntEnum):
    active = ActivatorModel.ACTIVE_STATUS
    inactive = ActivatorModel.INACTIVE_STATUS

@dataclass(kw_only=True, frozen=True, slots=True)
class Category(Entity):
    title: str
    slug: Optional[str] = ""
    description: Optional[str] = ""
    status: Optional[StatusEnum] = StatusEnum.active
    is_deleted: bool = False
    created_at: Optional[datetime] = field(default_factory=lambda: now())

    def update(self, data: dict):
        for field_name, value in data.items():
            self._set(field_name, value)

    def _set(self, field_name, value):
        object.__setattr__(self, field_name, value)

        return self

    def activate(self):
        self._set('status', ActivatorModel.ACTIVE_STATUS)

    def deactivate(self):
        self._set('status', ActivatorModel.INACTIVE_STATUS)

    @classmethod
    def validate(cls, data: Dict[str, Any]):
        validator = CategoryValidatorFactory.create()
        return validator.validate(serializer_class=CategorySerializer, data=data)
