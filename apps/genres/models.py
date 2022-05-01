from django.db import models

# Third
from django_extensions.db.models import ActivatorModel, TimeStampedModel, TitleSlugDescriptionModel

# Apps
from apps.core.models import UUIDModel, SoftDeleteModel
from apps.core.managers import SoftDeleteAndInactiveManager
from apps.core.messages import GENRE as GENRE_TEXT
from apps.core.messages import GENRES
from apps.categories.models import Category


class Genre(
    TitleSlugDescriptionModel,
    UUIDModel,
    ActivatorModel,
    SoftDeleteModel,
    TimeStampedModel,
):
    categories = models.ManyToManyField(Category, through="GenreHasCategory")

    objects = SoftDeleteAndInactiveManager()

    def __str__(self):
        return f"{self.title}"

    class Meta:
        ordering = ["created"]
        verbose_name = GENRE_TEXT
        verbose_name_plural = GENRES


class GenreHasCategory(models.Model):
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return "{}_{}".format(self.genre.__str__(), self.category.__str__())
