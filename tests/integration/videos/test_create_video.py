# Python
from unittest.mock import patch

# Third
import pytest

# Apps
from tests import factories
from apps.videos.views import create_video
from apps.videos.models import Video
from apps.videos.serializers import VideoCreateSerializer


def make_video_data():
    video_data = factories.VideoFactory.build()
    genre = factories.GenreWithCategoryFactory.create()
    category_pk = genre.categories.first().pk

    return {
        "title": video_data.title,
        "description": "some item",
        "categories": [
            category_pk,
        ],
        "genres": [genre.pk.__str__()],
        "year_launched": video_data.year_launched,
        "rating": video_data.rating,
        "duration": video_data.duration,
    }


@pytest.mark.django_db(reset_sequences=True)
@pytest.mark.integration
@patch("apps.videos.events.VideoCreated.run")
def test_create_video_call_tasks(run_mocked):
    serializer_class = VideoCreateSerializer
    data = make_video_data()
    serializer = serializer_class(data=data)
    serializer.is_valid()

    instance = create_video(serializer=serializer)
    run_mocked.assert_called_once()


@pytest.mark.django_db(reset_sequences=True)
@pytest.mark.integration
@patch("apps.videos.events.VideoCreated.run")
def test_create_video_returns_an_instance(run_mocked):
    serializer_class = VideoCreateSerializer
    data = make_video_data()
    serializer = serializer_class(data=data)
    serializer.is_valid()

    instance = create_video(serializer=serializer)
    run_mocked.assert_called_once()

    assert isinstance(instance, Video)
