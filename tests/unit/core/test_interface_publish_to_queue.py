import pytest
from django.test import override_settings
from unittest.mock import patch

from src.core.infrastructure.rabbitmq import InterfacePublishToQueue


@pytest.mark.integration
@override_settings(AMQP_URI='amqp://guest:guest@some-test/')
@pytest.mark.skip
def test_interface():
    pass


@pytest.mark.integration
@override_settings(AMQP_URI='amqp://guest:guest@some-test/')
@pytest.mark.skip
def test_close_channel():
    pass


@pytest.mark.integration
@override_settings(AMQP_URI='amqp://guest:guest@some-test/')
@pytest.mark.skip
def test_close_connection():
    pass


@pytest.mark.integration
@override_settings(AMQP_URI='amqp://guest:guest@some-test/')
@pytest.mark.skip
def test_teardown():
    pass


@pytest.mark.integration
@override_settings(AMQP_URI='amqp://guest:guest@some-test/')
@pytest.mark.skip
def test_message_to_json():
    pass


@pytest.mark.integration
@override_settings(AMQP_URI='amqp://guest:guest@some-test/')
@pytest.mark.skip
def test_run():
    pass
