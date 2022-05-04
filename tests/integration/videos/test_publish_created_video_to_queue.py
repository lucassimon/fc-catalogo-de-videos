# Python
from unittest.mock import patch

from django.test import override_settings

# Third
import pytest

# Apps
from src.videos.infrastructure.publish_video_to_queue import PublishCreatedVideoToQueue


@pytest.mark.integration
@override_settings(AMQP_URI='amqp://guest:guest@some-test/')
@pytest.mark.skip
def test_constructor():
    pass


@pytest.mark.skip
def test_connect():
    pass
