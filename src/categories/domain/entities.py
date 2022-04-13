# Python
from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional

# Third
from django_extensions.db.models import ActivatorModel

# Apps
from src.core.domain import entities
from apps.core.utils import now


@dataclass(kw_only=True, frozen=True, slots=True)
class Category(entities.Entity):
    title: str
    slug: str
    description: Optional[str] = ""
    status: Optional[int] = ActivatorModel.ACTIVE_STATUS
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
