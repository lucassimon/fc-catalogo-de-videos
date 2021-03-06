# Third
from rest_framework import serializers
from rest_framework.fields import UUIDField

# Apps
from apps.genres import models
from apps.categories.models import Category


class GenreSerializer(serializers.ModelSerializer):
    categories = serializers.PrimaryKeyRelatedField(
        many=True,
        pk_field=UUIDField(format="hex_verbose"),
        queryset=Category.objects.active().undeleted(),
    )

    class Meta:
        model = models.Genre
        fields = ["id", "categories", "title", "status", "slug", "is_deleted", "description", "created"]
