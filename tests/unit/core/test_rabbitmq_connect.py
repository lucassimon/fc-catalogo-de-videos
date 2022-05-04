# Python
from unittest.mock import patch

from django.test import override_settings

# Third
import pytest

# Apps
from src.core.infrastructure.rabbitmq import RabbitMQ


@pytest.mark.integration
@override_settings(AMQP_URI='amqp://guest:guest@some-test/')
@pytest.mark.skip
def test_check_amqp_uri(blocking_connection_mock, url_parameters_mock):
    pass
