# Third
from rest_framework import filters, viewsets
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend

# Apps
from apps.categories import models, serializers


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CategorySerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ["status", "is_deleted"]
    search_fields = [
        "title",
    ]
    ordering_fields = [
        "id",
        "created",
    ]

    @extend_schema(
        request=serializers.CategorySerializer,
        responses={201: serializers.CategorySerializer},
        tags=["Categories"],
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(
        request=serializers.CategorySerializer,
        responses={201: serializers.CategorySerializer},
        tags=["Categories"],
    )
    def list(self, request, *args, **kwargs):
        if "no_page" in request.query_params:
            self._paginator = None
        return super().list(request, *args, **kwargs)

    @extend_schema(
        request=serializers.CategorySerializer,
        responses={201: serializers.CategorySerializer},
        tags=["Categories"],
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        request=serializers.CategorySerializer,
        responses={200: serializers.CategorySerializer},
        tags=["Categories"],
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(
        request=serializers.CategorySerializer,
        responses={200: serializers.CategorySerializer},
        tags=["Categories"],
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(
        request=serializers.CategorySerializer,
        responses={200: serializers.CategorySerializer},
        tags=["Categories"],
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    def get_object(self):
        obj = super().get_object()
        return obj

    def get_queryset(self):
        queryset = models.Category.objects.all()
        return queryset

    def perform_destroy(self, instance):
        instance.soft_delete()
