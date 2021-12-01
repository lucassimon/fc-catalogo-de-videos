from rest_framework import serializers

from apps.categories import models


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ["id", "code", "title", "slug", "description", "created"]
