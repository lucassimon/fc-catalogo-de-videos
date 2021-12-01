from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework import filters

from apps.categories import models, serializers


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    permission_classes = [AllowAny]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = [
        "title",
    ]
    ordering_fields = [
        "id",
        "created",
    ]
