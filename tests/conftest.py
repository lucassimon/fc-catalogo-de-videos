import pytest
import tempfile

from pytest_factoryboy import register
from django_extensions.db.models import ActivatorModel
from PIL import Image

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


@pytest.fixture
def api_client():
    from rest_framework.test import APIClient

    return APIClient()
