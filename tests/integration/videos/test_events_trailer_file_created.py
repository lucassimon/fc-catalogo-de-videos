# Python
from unittest.mock import patch

# Third
import pytest

# Apps
from tests import factories
from apps.videos.events import VideoCreatedTrailerFileTasks


@pytest.mark.django_db(reset_sequences=True)
@pytest.mark.integration
def test_make_message():
    video = factories.VideoFactory.create(with_files=True, title="Test Str")
    result = VideoCreatedTrailerFileTasks().make_message(video)

    expected = {
        "action": "created",
        "field": "trailer_file",
        "video": {
            "id": f"{video.id}",
            "trailer_file": video.trailer_file.url,
        }
    }

    assert result == expected


@pytest.mark.django_db(reset_sequences=True)
@pytest.mark.integration
def test_send_with_no_trailer_file(_):
    video = factories.VideoFactory.create(title="Test Str")
    result = VideoCreatedTrailerFileTasks().send(video)

    assert result is None


@pytest.mark.django_db(reset_sequences=True)
@pytest.mark.integration
@patch('apps.videos.tasks.celery_send_message_to_created_video_queue.apply_async')
def test_send_with_no_trailer_file(celery_method):
    video = factories.VideoFactory.create(with_files=True, title="Test Str")
    message = VideoCreatedTrailerFileTasks().make_message(video)
    VideoCreatedTrailerFileTasks().send(video)


    celery_method.assert_called_with((message,))
