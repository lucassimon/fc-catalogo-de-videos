# Third
from rest_framework import filters, viewsets
from rest_framework.permissions import AllowAny

# Apps
from apps.castmembers import models, serializers
from apps.core import utils


class CastMemberViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CastMemberSerializer
    permission_classes = [AllowAny]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = [
        "name",
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
        qs = models.CastMember.objects.all().undeleted()

        return qs

    def perform_destroy(self, instance):
        instance.soft_delete()
