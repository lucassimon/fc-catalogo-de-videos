import pytest
from unittest.mock import patch
from tests import factories
from django_extensions.db.models import ActivatorModel

from apps.videos.tasks import VideoTasks


@pytest.mark.django_db(reset_sequences=True)
@pytest.mark.integration
@patch('apps.videos.tasks.VideoTasks.send_message_to_created_video_queue')
def test_params(mock_task):
    video = factories.VideoFactory.create(title="Test Str")
    VideoTasks.send_message_to_created_video_queue(video)
    mock_task.assert_called_with(video)


@pytest.mark.django_db(reset_sequences=True)
@pytest.mark.integration
def test_raises_exception_when_video_is_deleted():
    video = factories.VideoFactory.create(title="Test Str", is_deleted=True)

    with pytest.raises(Exception) as assert_error:
        VideoTasks.send_message_to_created_video_queue(video)

    assert assert_error.value.args[0] == "Video created with deleted attribute"


@pytest.mark.django_db(reset_sequences=True)
@pytest.mark.integration
def test_raises_exception_when_status_inactive():
    video = factories.VideoFactory.create(title="Test Str", status=ActivatorModel.INACTIVE_STATUS)

    with pytest.raises(Exception) as assert_error:
        VideoTasks.send_message_to_created_video_queue(video)

    assert assert_error.value.args[0] == "Video created with inactive status"


@pytest.mark.django_db(reset_sequences=True)
@pytest.mark.integration
def test_raises_exception_when_trailer_is_none():
    video = factories.VideoFactory.create(title="Test Str", trailer_file=None)

    with pytest.raises(Exception) as assert_error:
        VideoTasks.send_message_to_created_video_queue(video)

    assert assert_error.value.args[0] == "Trailer or original file was not uploaded"


@pytest.mark.django_db(reset_sequences=True)
@pytest.mark.integration
def test_create_message():
    video = factories.VideoFactory.create(with_files=True)

    result = VideoTasks.make_message(video)

    thumb = f"/media/catalago-de-videos/{video.id}/thumb/thumb.png"
    banner = f"/media/catalago-de-videos/{video.id}/banner/banner.png"
    trailler = f"/media/catalago-de-videos/{video.id}/trailer/trailler.mp4"
    video_url = f"/media/catalago-de-videos/{video.id}/videos/video.mpeg"

    assert result == {
            "action": "created",
            "video": {
                "id": f"{video.id}",
                "thumb_file": thumb,
                "banner_file": banner,
                "trailer_file": trailler,
                "video_file": video_url,
            }
        }

@pytest.mark.django_db(reset_sequences=True)
@pytest.mark.integration
@patch('apps.videos.tasks.VideoTasks.send_message_to_created_video_queue', return_value=1)
def test_task_send_message_to_created_video_queue(mock_task):
    video = factories.VideoFactory.create(with_files=True, title="Test Str")
    result = VideoTasks.send_message_to_created_video_queue(video)
    mock_task.assert_called_with(video)
    assert 1 == result

