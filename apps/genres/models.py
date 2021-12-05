from django.db import models

# Third
from django_extensions.db.models import (
    ActivatorModel,
    TimeStampedModel,
    TitleSlugDescriptionModel,
)

# Apps
from apps.categories.models import Category
from apps.core.managers import SoftDeleteAndInactiveManager
from apps.core.messages import GENRE as GENRE_TEXT
from apps.core.messages import GENRES
from apps.core.models import SoftDeleteModel, UUIDModel


class Genre(
    TitleSlugDescriptionModel,
    UUIDModel,
    ActivatorModel,
    SoftDeleteModel,
    TimeStampedModel,
):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    objects = SoftDeleteAndInactiveManager()

    def __str__(self):
        return f"{self.title}"

    class Meta:
        ordering = ["created"]
        verbose_name = GENRE_TEXT
        verbose_name_plural = GENRES
        indexes = [
            models.Index(
                fields=[
                    "code",
                ]
            ),
        ]
