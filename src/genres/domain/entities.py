"""
Define uma entidade
"""
# Python
from typing import Optional
from datetime import datetime
from dataclasses import field, dataclass

# Third
from django_extensions.db.models import ActivatorModel

# Apps
from apps.core.utils import now, uuidv4


@dataclass()
class Genre:
    """
    Representa os dados da entidade genero
    """

    title: str
    slug: str
    status: Optional[int] = ActivatorModel.ACTIVE_STATUS
    is_deleted: bool = False
    code: Optional[str] = field(default_factory=uuidv4)
    created_at: Optional[datetime] = field(default_factory=now)
