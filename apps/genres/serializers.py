# Third
from rest_framework import serializers
from rest_framework.fields import UUIDField

# Apps
from apps.categories.models import Category
from apps.genres import models


class GenreSerializer(serializers.ModelSerializer):
    categories = serializers.PrimaryKeyRelatedField(many=True, pk_field=UUIDField(format='hex_verbose'), queryset=Category.objects.active().undeleted())

    class Meta:
        model = models.Genre
        fields = ["id", "categories", "title", "slug", "description", "created"]
