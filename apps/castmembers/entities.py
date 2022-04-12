# Python
from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional

# Third
from django_extensions.db.models import ActivatorModel

# Apps
from apps.castmembers.models import CastMemberModel
from apps.core.utils import now, uuidv4


@dataclass()
class CastMember:
    name: str
    kind: str = CastMemberModel.KIND_DIRECTOR
    status: Optional[int] = ActivatorModel.ACTIVE_STATUS
    is_deleted: bool = False
    code: Optional[str] = field(default_factory=lambda: uuidv4())
    created_at: Optional[datetime] = field(default_factory=lambda: now())
