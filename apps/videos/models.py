from django.db import models

# Third
from django_extensions.db.models import ActivatorModel, TimeStampedModel, TitleSlugDescriptionModel

# Apps
from apps.categories.models import Category
from apps.core.managers import SoftDeleteAndInactiveManager
from apps.core.messages import (
    DURATION,
    EIGHTEEN_YEARS_OLD,
    FOURTEEN_YEARS_OLD,
    FREE,
    OPENED,
    RATING,
    SIXTEEN_YEAR_OLD,
    TEN_YEARS_OLD,
    TWELVE_YEARS_OLD,
)
from apps.core.messages import VIDEO as VIDEO_TEXT
from apps.core.messages import VIDEOS, YEAR_LAUNCHED
from apps.core.models import SoftDeleteModel, UUIDModel
from apps.genres.models import Genre

# Local
from .views import banner_upload_to_path, thumb_upload_to_path, trailer_upload_to_path, video_upload_to_path


class Video(
    TitleSlugDescriptionModel,
    UUIDModel,
    ActivatorModel,
    SoftDeleteModel,
    TimeStampedModel,
):

    RATING_FREE = "F"
    RATING_TEN_YEARS = "10"
    RATING_TWELVE_YEARS = "12"
    RATING_FOURTEEN_YEARS = "14"
    RATING_SIXTEEN_YEAR = "16"
    RATING_EIGHTEEN_YEARS = "18"

    RATING_CHOICES = (
        (RATING_FREE, FREE),
        (RATING_TEN_YEARS, TEN_YEARS_OLD),
        (RATING_TWELVE_YEARS, TWELVE_YEARS_OLD),
        (RATING_FOURTEEN_YEARS, FOURTEEN_YEARS_OLD),
        (RATING_SIXTEEN_YEAR, SIXTEEN_YEAR_OLD),
        (RATING_EIGHTEEN_YEARS, EIGHTEEN_YEARS_OLD),
    )

    THUMB_FILE_MAX_SIZE = 1024 * 5
    BANNER_FILE_MAX_SIZE = 1024 * 10
    TRAILER_FILE_MAX_SIZE = 1024 * 1024 * 1
    VIDEO_FILE_MAX_SIZE = 1024 * 1024 * 50  # 50GB

    categories = models.ManyToManyField(Category)
    genres = models.ManyToManyField(Genre)

    year_launched = models.PositiveSmallIntegerField(YEAR_LAUNCHED)
    opened = models.BooleanField(OPENED, default=False)
    rating = models.CharField(
        RATING, max_length=2, choices=RATING_CHOICES, default=RATING_FREE
    )
    duration = models.PositiveSmallIntegerField(DURATION)

    thumb_file = models.ImageField(
        upload_to=thumb_upload_to_path, blank=True, null=True
    )
    banner_file = models.ImageField(
        upload_to=banner_upload_to_path, blank=True, null=True
    )
    trailer_file = models.FileField(
        upload_to=trailer_upload_to_path, blank=True, null=True
    )
    video_file = models.FileField(upload_to=video_upload_to_path, blank=True, null=True)

    objects = SoftDeleteAndInactiveManager()

    def __str__(self):
        return f"{self.title}"

    class Meta:
        ordering = ["created"]
        verbose_name = VIDEO_TEXT
        verbose_name_plural = VIDEOS
