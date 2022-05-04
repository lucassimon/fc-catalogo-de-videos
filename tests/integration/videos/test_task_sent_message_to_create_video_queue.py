# Python
from unittest.mock import patch

# Third
import pytest

# Apps
from apps.videos.tasks import celery_send_message_to_created_video_queue


class StubSomeConnection:
    pass


class StubSomeChannel:
    def queue_declare(self, *args, **kwargs):
        pass

    def queue_bind(self, *args, **kwargs):
        pass

    def confirm_delivery(self):
        pass


@pytest.mark.django_db(reset_sequences=True)
@pytest.mark.integration
@patch('src.videos.infrastructure.publish_video_to_queue.PublishCreatedVideoToQueue.run')
@patch('src.core.infrastructure.rabbitmq.RabbitMQ.connect', return_value=(StubSomeConnection(), StubSomeChannel()))
def test_task_send_message_to_created_video_queue(mock_connect, mock_run):
    message = {'foo': 'bar'}
    celery_send_message_to_created_video_queue(message)

    mock_connect.assert_called_once()
    mock_run.assert_called_with(message)
