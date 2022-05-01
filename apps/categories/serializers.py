# Python
from unittest.util import _MAX_LENGTH

# Third
from rest_framework import serializers

# Apps
from apps.categories import models
from apps.core.fields import StrictCharField, StrictBooleanField


class CategorySerializer(serializers.ModelSerializer):
    title = StrictCharField(max_length=255)
    description = StrictCharField(required=False, max_length=255, allow_null=True, allow_blank=True)
    is_deleted = StrictBooleanField(required=False)

    class Meta:
        model = models.Category
        fields = [
            "id",
            "title",
            "slug",
            "description",
            "status",
            "is_deleted",
            "created",
        ]
