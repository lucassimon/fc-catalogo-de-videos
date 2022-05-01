import pytest
from django.test import override_settings
from unittest.mock import patch

from src.core.infrastructure.rabbitmq import RabbitMQ


@pytest.mark.integration
@override_settings(AMQP_URI='amqp://guest:guest@some-test/')
@pytest.mark.skip
def test_check_amqp_uri(blocking_connection_mock, url_parameters_mock):
    pass
