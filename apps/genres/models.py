from django.db import models
from django_extensions.db.models import (
    TitleSlugDescriptionModel,
    ActivatorModel,
    TimeStampedModel,
)
from apps.core.models import SoftDeleteModel, UUIDModel
from apps.core.messages import GENRES, GENRE as GENRE_TEXT
from apps.core.managers import SoftDeleteAndInactiveManager
from apps.categories.models import Category


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
