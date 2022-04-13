# Python
import dataclasses
from datetime import datetime
from typing import Optional

# Third
from django_extensions.db.models import ActivatorModel
from pydantic import BaseModel, constr

from pydantic.dataclasses import dataclass
from enum import IntEnum
# Apps
from src.core.domain import entities
from apps.core.utils import now

class StatusEnum(IntEnum):
    active = ActivatorModel.ACTIVE_STATUS
    inactive = ActivatorModel.INACTIVE_STATUS

@dataclass(frozen=True)
class Category:
    title: constr(min_length=5, max_length=255)
    slug: constr(min_length=5, max_length=255)
    description: Optional[str] = ""
    status: Optional[StatusEnum] = StatusEnum.active
    is_deleted: bool = False
    created_at: Optional[datetime] = dataclasses.field(default_factory=lambda: now())

    class Config:
        allow_mutation = False

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
