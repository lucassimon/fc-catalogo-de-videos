from django.db import models

# Third
from django_extensions.db.models import ActivatorQuerySet

# Apps
from apps.core.models import SoftDeleteQuerySet


class SoftDeleteAndInactiveQueryset(ActivatorQuerySet, SoftDeleteQuerySet):
    pass


class SoftDeleteAndInactiveManager(models.Manager):
    def get_queryset(self):
        return SoftDeleteAndInactiveQueryset(self.model, using=self._db)

    def active(self):
        return self.get_queryset().active()

    def inactive(self):
        return self.get_queryset().inactive()

    def deleted(self):
        return self.get_queryset().deleted()

    def undeleted(self):
        return self.get_queryset().undeleted()
