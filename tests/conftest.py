import pytest
import factory

from pytest_factoryboy import register
from django_extensions.db.models import ActivatorModel

from apps.castmembers import models

from tests.factories.categories import CategoryFactory
from tests.factories.genres import GenreFactory, GenreWithCategoryFactory
from tests.factories.cast_members import CastMemberFactory
from tests.factories.videos import VideoFactory

register(CategoryFactory)
register(CategoryFactory, "category_inactive", status=ActivatorModel.INACTIVE_STATUS)
register(CategoryFactory, "category_deleted", is_deleted=True)
register(GenreFactory)
register(GenreWithCategoryFactory)
register(CastMemberFactory)
register(CastMemberFactory, "director_cast_member", kind=models.CastMember.KIND_DIRECTOR)
register(CastMemberFactory, "cast_member_deleted", is_deleted=True)
register(VideoFactory)
register(VideoFactory, "video_inactive", status=ActivatorModel.INACTIVE_STATUS)
register(VideoFactory, "video_deleted", is_deleted=True)
register(
    VideoFactory,
    "video_with_files",
    thumb_file=factory.django.ImageField(width=200, height=200),
    banner_file=factory.django.ImageField(width=200, height=200),
    trailer_file=factory.django.FileField(filename="trailler.mp4"),
    video_file=factory.django.FileField(filename="video.mpeg"),
)


@pytest.fixture
def api_client():
    from rest_framework.test import APIClient

    return APIClient()
