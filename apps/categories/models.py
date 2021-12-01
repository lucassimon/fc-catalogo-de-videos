from django.utils.translation import ugettext_lazy as _

from django.db import models
from django_extensions.db.models import (
    TitleSlugDescriptionModel,
    ActivatorModel,
    TimeStampedModel,
)
from apps.core.models import SoftDeleteModel, UUIDModel
from apps.core.messages import CATEGORIES, CATEGORY as CATEGORY_TEXT


class Category(
    TitleSlugDescriptionModel,
    UUIDModel,
    ActivatorModel,
    SoftDeleteModel,
    TimeStampedModel,
):
    def __str__(self):
        return f"{self.title}"

    class Meta:
        """
        Seta a ordenação da listagem pelo campo `created` ascendente
        """

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
