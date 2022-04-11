# Third
from rest_framework import filters, viewsets
from rest_framework.permissions import AllowAny

# Apps
from apps.videos import models, serializers, views
from apps.core import utils

# debug
import ipdb


class VideoViewSet(viewsets.ModelViewSet):
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
        qs = models.Video.objects.active().undeleted()

        return qs

    def perform_create(self, serializer):
        views.create_video(serializer)

    def perform_update(self, serializer):
        views.create_video(serializer)

    def perform_destroy(self, instance):
        views.delete_video(instance)

    def get_serializer_class(self):
        if self.request.method in ["PUT", "PATCH"]:
            return serializers.VideoUpdateSerializer
        else:
            return serializers.VideoCreateSerializer
