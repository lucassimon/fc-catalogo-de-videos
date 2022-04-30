# Third
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets
from rest_framework.permissions import AllowAny
from drf_spectacular.utils import OpenApiExample, OpenApiParameter, extend_schema

# Apps
from apps.videos import models, serializers, views


class VideoViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ["status", "opened", "is_deleted", "rating"]
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
        qs = models.Video.objects.all()
        return qs

    @extend_schema(
        request=serializers.VideoCreateSerializer,
        responses={201: serializers.VideoCreateSerializer},
        tags=["Categories"],
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

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
