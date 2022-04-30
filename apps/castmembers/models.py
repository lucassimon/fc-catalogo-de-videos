from django.db import models

# Third
from django_extensions.db.models import TimeStampedModel

# Apps
from apps.core.managers import SoftDeleteAndInactiveManager
from apps.core.messages import ACTOR, CAST_MEMBER, CAST_MEMBERS, DIRECTOR, KIND, NAME
from apps.core.models import SoftDeleteModel, UUIDModel


class CastMember(UUIDModel, SoftDeleteModel, TimeStampedModel):

    KIND_DIRECTOR = 0
    KIND_ACTOR = 1

    KIND_CHOICES = (
        (KIND_DIRECTOR, DIRECTOR),
        (KIND_ACTOR, ACTOR),
    )

    name = models.CharField(NAME, max_length=255)
    kind = models.IntegerField(KIND, choices=KIND_CHOICES, default=KIND_ACTOR)

    objects = SoftDeleteAndInactiveManager()

    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ["created"]
        verbose_name = CAST_MEMBER
        verbose_name_plural = CAST_MEMBERS
