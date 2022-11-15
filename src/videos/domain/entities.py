"""
Define entidades para os videos
"""

# Python
from typing import Optional
from datetime import datetime
from dataclasses import field, dataclass

# Third
from django_extensions.db.models import ActivatorModel

# Apps
from apps.core.utils import now, uuidv4
from apps.videos.models import Video as VideoModel


@dataclass()
class Video:
    """
    Entity for a Video
    """

    title: str
    slug: str
    year_launched: int = 2022
    opened: bool = True
    rating: str = VideoModel.RATING_EIGHTEEN_YEARS
    duration: int = 50
    status: Optional[int] = ActivatorModel.ACTIVE_STATUS
    is_deleted: bool = False
    code: Optional[str] = field(default_factory=uuidv4)
    thumb_file: Optional[str] = ""
    banner_file: Optional[str] = ""
    trailer_file: Optional[str] = ""
    video_file: Optional[str] = ""
    created_at: Optional[datetime] = field(default_factory=now)
