import pytest
from unittest.mock import patch

from apps.videos.views import create_video
from apps.videos.models import Video
from apps.videos.serializers import VideoCreateSerializer

from tests import factories


def make_video_data():
    video_data = factories.VideoFactory.build()
    genre = factories.GenreWithCategoryFactory.create()
    category_pk = genre.categories.first().pk

    return {
        "title": video_data.title,
        "description": "some item",
        "categories": [category_pk,],
        "genres": [genre.pk.__str__()],
        "year_launched": video_data.year_launched,
        "rating": video_data.rating,
        "duration": video_data.duration,
    }


@pytest.mark.django_db(reset_sequences=True)
@pytest.mark.integration
@patch("apps.videos.tasks.VideoTasks.send_message_to_created_video_queue.apply_async", return_value="task-id")
def test_create_video_call_taks(apply_async):
    serializer_class = VideoCreateSerializer
    data = make_video_data()
    serializer = serializer_class(data=data)
    serializer.is_valid()

    instance = create_video(serializer=serializer)
    apply_async.assert_called_with((instance,),)


@patch("apps.videos.tasks.VideoTasks.send_message_to_created_video_queue.apply_async", return_value="task-id")
@pytest.mark.django_db(reset_sequences=True)
@pytest.mark.integration
def test_create_video_returns_an_instance(apply_async):
    serializer_class = VideoCreateSerializer
    data = make_video_data()
    serializer = serializer_class(data=data)
    serializer.is_valid()

    instance = create_video(serializer=serializer)
    apply_async.assert_called_with((instance,),)

    assert isinstance(instance, Video)
