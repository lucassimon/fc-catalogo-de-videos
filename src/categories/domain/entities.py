# Python
from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, Optional

# Third
import ipdb
from devtools import debug as ddebug
from django_extensions.db.models import ActivatorModel

# Apps
from apps.categories.serializers import CategorySerializer
from apps.core.utils import now
from src.categories.domain.factories import CategoryValidatorFactory
from src.core.domain.entities import Entity
from src.core.domain.exceptions import EntityValidationException


@dataclass(kw_only=True, frozen=True, slots=True)
class Category(Entity):
    title: str
    slug: Optional[str] = ""
    description: Optional[str] = ""
    status: Optional[int] = ActivatorModel.ACTIVE_STATUS
    is_deleted: bool = False
    created_at: Optional[datetime] = field(default_factory=lambda: now())

    def __post_init__(self):
        self.validate()

    def update(self, data: Dict[str, Any]):
        for field_name, value in data.items():
            self._set(field_name, value)

        self.validate()

    def _set(self, field_name, value):
        object.__setattr__(self, field_name, value)

        return self

    def activate(self):
        self._set('status', ActivatorModel.ACTIVE_STATUS)

    def deactivate(self):
        self._set('status', ActivatorModel.INACTIVE_STATUS)

    def validate(self):
        validator = CategoryValidatorFactory.create()
        is_valid = validator.validate(serializer_class=CategorySerializer, data=self.to_dict())
        if not is_valid:
            raise EntityValidationException(validator.errors)
