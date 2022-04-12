# Third
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiExample, OpenApiParameter, extend_schema
from rest_framework import filters, viewsets
from rest_framework.permissions import AllowAny

# Apps
from apps.castmembers import models, serializers


class CastMemberViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CastMemberSerializer
    permission_classes = [AllowAny]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = [
        "@name",
    ]
    ordering_fields = [
        "id",
        "created",
    ]

    def get_object(self):
        obj = super().get_object()

        return obj

    def get_queryset(self):
        qs = models.CastMember.objects.all()

        return qs

    @extend_schema(
        request=serializers.CastMemberSerializer,
        responses={201: serializers.CastMemberSerializer},
        tags=["Members"],
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(
        # extra parameters added to the schema
        parameters=[
            OpenApiParameter(
                name="created",
                type=OpenApiTypes.DATE,
                location=OpenApiParameter.QUERY,
                description="Filter by created date",
            ),
        ],
        # override default docstring extraction
        description="List all cast members",
        # provide Authentication class that deviates from the views default
        auth=None,
        # change the auto-generated operation name
        operation_id="list_cast_members",
        tags=["Members"],
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(
        request=serializers.CastMemberSerializer,
        responses={200: serializers.CastMemberSerializer},
        tags=["Members"],
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        request=serializers.CastMemberSerializer,
        responses={200: serializers.CastMemberSerializer},
        tags=["Members"],
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(
        request=serializers.CastMemberSerializer,
        responses={200: serializers.CastMemberSerializer},
        tags=["Members"],
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(
        request=serializers.CastMemberSerializer,
        responses={200: serializers.CastMemberSerializer},
        tags=["Members"],
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    def perform_destroy(self, instance):
        instance.soft_delete()
