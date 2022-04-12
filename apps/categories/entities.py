# Python
import uuid
from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional

# Third
from django_extensions.db.models import ActivatorModel

# Apps
from apps.core import entities
from apps.core.utils import now, uuidv4


@dataclass(kw_only=True, frozen=True)
class Category(entities.Entity):
    title: str
    slug: str
    description: Optional[str] = ""
    status: Optional[int] = ActivatorModel.ACTIVE_STATUS
    is_deleted: bool = False
    code: Optional[uuid.UUID] = field(default_factory=lambda: uuidv4())
    created_at: Optional[datetime] = field(default_factory=lambda: now())
