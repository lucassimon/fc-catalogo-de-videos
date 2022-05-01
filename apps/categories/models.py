from django.db import models

# Third
from django_extensions.db.models import ActivatorModel, TimeStampedModel, TitleSlugDescriptionModel

# Apps
from apps.core.models import UUIDModel, SoftDeleteModel
from apps.core.managers import SoftDeleteAndInactiveManager
from apps.core.messages import CATEGORY as CATEGORY_TEXT
from apps.core.messages import CATEGORIES


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
