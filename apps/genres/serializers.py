# Third
from rest_framework import serializers

# Apps
from apps.genres import models


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Genre
        fields = ["id", "code", "category", "title", "slug", "description", "created"]