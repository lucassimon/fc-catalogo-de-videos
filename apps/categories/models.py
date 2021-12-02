from django.utils.translation import ugettext_lazy as _

from django.db import models
from django_extensions.db.models import (
    TitleSlugDescriptionModel,
    ActivatorQuerySet,
    ActivatorModel,
    TimeStampedModel,
)
from apps.core.models import SoftDeleteModel, SoftDeleteQuerySet, UUIDModel
from apps.core.messages import CATEGORIES, CATEGORY as CATEGORY_TEXT


class CategoryQueryset(ActivatorQuerySet, SoftDeleteQuerySet):
    pass


class CategoryManager(models.Manager):
    def get_queryset(self):
        return CategoryQueryset(self.model, using=self._db)

    def active(self):
        return self.get_queryset().active()

    def inactive(self):
        return self.get_queryset().inactive()

    def deleted(self):
        return self.get_queryset().deleted()

    def undeleted(self):
        return self.get_queryset().undeleted()


class Category(
    TitleSlugDescriptionModel,
    UUIDModel,
    ActivatorModel,
    SoftDeleteModel,
    TimeStampedModel,
):

    objects = CategoryManager()

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
