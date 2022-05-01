# Third
from rest_framework import filters, viewsets
from drf_spectacular.utils import OpenApiExample, OpenApiParameter, extend_schema
from rest_framework.permissions import AllowAny

# Apps
from apps.genres import models, serializers


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

    @extend_schema(
        request=serializers.GenreSerializer,
        responses={201: serializers.GenreSerializer},
        tags=["Genres"],
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(
        request=serializers.GenreSerializer,
        responses={201: serializers.GenreSerializer},
        tags=["Genres"],
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(
        request=serializers.GenreSerializer,
        responses={201: serializers.GenreSerializer},
        tags=["Genres"],
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        request=serializers.GenreSerializer,
        responses={200: serializers.GenreSerializer},
        tags=["Genres"],
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(
        request=serializers.GenreSerializer,
        responses={200: serializers.GenreSerializer},
        tags=["Genres"],
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(
        request=serializers.GenreSerializer,
        responses={200: serializers.GenreSerializer},
        tags=["Genres"],
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    def get_object(self):
        obj = super().get_object()
        return obj

    def get_queryset(self):
        qs = models.Genre.objects.all()
        return qs

    def perform_destroy(self, instance):
        instance.soft_delete()
