import pytest
from django.test import override_settings
from unittest.mock import patch

from src.videos.infrastructure.publish_video_to_queue import PublishCreatedVideoToQueue


@pytest.mark.integration
@override_settings(AMQP_URI='amqp://guest:guest@some-test/')
@pytest.mark.skip
def test_constructor():
    pass


@pytest.mark.skip
def test_connect():
    pass
