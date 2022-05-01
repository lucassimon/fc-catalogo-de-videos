# Third
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import OpenApiExample, OpenApiParameter, extend_schema
from rest_framework import filters, viewsets
from rest_framework.permissions import AllowAny

# Apps
from apps.videos import models, serializers, views


class VideoViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
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
        tags=["Videos"],
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(
        request=serializers.VideoCreateSerializer,
        responses={201: serializers.VideoCreateSerializer},
        tags=["Videos"],
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(
        request=serializers.VideoCreateSerializer,
        responses={201: serializers.VideoCreateSerializer},
        tags=["Videos"],
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        request=serializers.VideoUpdateSerializer,
        responses={200: serializers.VideoCreateSerializer},
        tags=["Videos"],
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(
        request=serializers.VideoUpdateSerializer,
        responses={200: serializers.VideoCreateSerializer},
        tags=["Videos"],
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(
        request=serializers.VideoUpdateSerializer,
        responses={200: serializers.VideoCreateSerializer},
        tags=["Videos"],
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

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
