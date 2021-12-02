from rest_framework import viewsets, status, filters
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

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

    def get_queryset(self):
        qs = models.Category.objects.active().undeleted()

        return qs

    def destroy(self, request, *args, **kwargs):
        object = self.get_object()
        object.soft_delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
