import uuid
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class UUIDModel(models.Model):
    code = models.UUIDField(default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class SoftDeleteQuerySet(models.query.QuerySet):
    def deleted(self):
        return self.filter(is_deleted=True)

    def undeleted(self):
        return self.filter(is_deleted=False)


class SoftDeleteManager(models.Manager):
    def get_queryset(self):
        return SoftDeleteQuerySet(model=self.model, using=self._db)

    def deleted(self):
        return self.get_queryset().deleted()

    def undeleted(self):
        return self.get_queryset().undeleted()


class SoftDeleteModel(models.Model):
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(blank=True, null=True, default=None)
    objects = SoftDeleteManager()
    all_objects = models.Manager()

    def soft_delete(self):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()

    def restore(self):
        self.is_deleted = False
        self.deleted_at = None
        self.save()

    class Meta:
        abstract = True
