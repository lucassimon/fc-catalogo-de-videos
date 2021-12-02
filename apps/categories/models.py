from django.db import models
from django_extensions.db.models import (
    TitleSlugDescriptionModel,
    ActivatorModel,
    TimeStampedModel,
)
from apps.core.models import SoftDeleteModel, UUIDModel
from apps.core.messages import CATEGORIES, CATEGORY as CATEGORY_TEXT
from apps.core.managers import SoftDeleteAndInactiveManager


class Category(
    TitleSlugDescriptionModel,
    UUIDModel,
    ActivatorModel,
    SoftDeleteModel,
    TimeStampedModel,
):

    objects = SoftDeleteAndInactiveManager()

    def __str__(self):
        return f"{self.title}"

    class Meta:
        ordering = ["created"]
        verbose_name = CATEGORY_TEXT
        verbose_name_plural = CATEGORIES
        indexes = [
            models.Index(
                fields=[
                    "code",
                ]
            ),
        ]
