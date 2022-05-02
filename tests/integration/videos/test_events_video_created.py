import pytest
from tests import factories
from django_extensions.db.models import ActivatorModel
from unittest.mock import patch

from apps.videos.events import VideoCreated


@pytest.mark.django_db(reset_sequences=True)
@pytest.mark.integration
def test_raises_exception_when_video_is_deleted():
    video = factories.VideoFactory.create(title="Test Str", is_deleted=True)

    with pytest.raises(Exception) as assert_error:
        VideoCreated(video.id.__str__())

    assert assert_error.value.args[0] == "Video created with deleted attribute"


@pytest.mark.django_db(reset_sequences=True)
@pytest.mark.integration
def test_raises_exception_when_status_inactive():
    video = factories.VideoFactory.create(title="Test Str", status=ActivatorModel.INACTIVE_STATUS)

    with pytest.raises(Exception) as assert_error:
        VideoCreated(video.id.__str__())

    assert assert_error.value.args[0] == "Video created with inactive status"


@pytest.mark.django_db(reset_sequences=True)
@pytest.mark.integration
@patch('apps.videos.events.VideoCreatedTrailerFileTasks.send')
@patch('apps.videos.events.VideoCreatedVideoFileTasks.send')
def test_run(video_file_mock, trailer_file_mock):
    video = factories.VideoFactory.create(with_files=True, title="Test Str")
    event = VideoCreated(video.id.__str__())
    event.run()

    video_file_mock.assert_called_with(video)
    trailer_file_mock.assert_called_with(video)

