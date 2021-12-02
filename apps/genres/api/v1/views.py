from rest_framework import viewsets, filters
from rest_framework.permissions import AllowAny


from apps.genres import models, serializers
from apps.core import utils


class GenreViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.GenreSerializer
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
        utils.raises_not_found_when_inactive_or_deleted(obj)

        return obj

    def get_queryset(self):
        qs = models.Genre.objects.active().undeleted()

        return qs

    def perform_destroy(self, instance):
        instance.soft_delete()
