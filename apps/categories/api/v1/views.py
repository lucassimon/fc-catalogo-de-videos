# Third
from rest_framework import filters, viewsets
from rest_framework.permissions import AllowAny

# Apps
from apps.categories import models, serializers


class CategoryViewSet(viewsets.ModelViewSet):
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

    def get_object(self):
        obj = super().get_object()
        return obj

    def get_queryset(self):
        qs = models.Category.objects.all()
        return qs

    def perform_destroy(self, instance):
        instance.soft_delete()
