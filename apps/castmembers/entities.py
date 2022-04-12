from datetime import datetime
from dataclasses import dataclass, field
from typing import Optional

from django_extensions.db.models import ActivatorModel

from apps.core.utils import now, uuidv4
from apps.castmembers.models import CastMemberModel


@dataclass()
class CastMember:
    name: str
    kind: str = CastMemberModel.KIND_DIRECTOR
    status: Optional[int] = ActivatorModel.ACTIVE_STATUS
    is_deleted: bool = False
    code: Optional[str] = field(default_factory=lambda: uuidv4())
    created_at: Optional[datetime] = field(default_factory=lambda: now())
