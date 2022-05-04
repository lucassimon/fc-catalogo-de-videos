# Python
from abc import ABC, abstractmethod
from json import dumps

from django.conf import settings

# Third
import pika
from pika import URLParameters, BlockingConnection


class RabbitMQ:
    @staticmethod
    def connect():
        params = URLParameters(settings.AMQP_URI)
        # number of socket connection attempts
        params.connection_attempts = 7
        # interval between socket connection attempts; see also connection_attempts.
        params.retry_delay = 300
        # AMQP connection heartbeat timeout value for negotiation during connection
        # tuning or callable which is invoked during connection tuning
        params.heartbeat = 600
        # None or float blocked connection timeout
        params.blocked_connection_timeout = 300
        try:
            connect = BlockingConnection(params)
            channel = connect.channel()

            return connect, channel

        except Exception as e:
            raise e


class InterfacePublishToQueue(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def publish(self, message: dict):
        pass

    def close_channel(self):
        self.channel.close()

    def close_connection(self):
        self.conn.close()

    def teardown(self):
        self.close_channel()
        self.close_connection()

    def run(self, message):
        self.connect()
        self.publish(message)

    def message_to_json(self, message):
        try:
            body = dumps(message)
            return body
        except Exception as e:
            raise e


class InterfaceRabbitMQ(InterfacePublishToQueue):
    def connect(self):
        if self.exchange_dlx and self.queue_dl and self.routing_key_dl:
            arguments = {
                "x-dead-letter-exchange": self.exchange_dlx,
                "x-dead-letter-routing-key": self.routing_key_dl,
            }
        else:
            arguments = {}

        self.channel.queue_declare(queue=self.queue, durable=True, arguments=arguments)
        self.channel.queue_bind(self.queue, self.exchange, routing_key=self.routing_key)
        # Turn on delivery confirmations
        self.channel.confirm_delivery()

    def publish(self, message: dict):
        """
        Publish a message in default exchange
        """

        properties = pika.BasicProperties(
            app_id="admin-catalog-video", content_type="application/json", delivery_mode=pika.DeliveryMode.Persistent
        )

        body = self.message_to_json(message)

        # Send a message
        try:
            self.channel.basic_publish(
                exchange=self.exchange,
                routing_key=self.routing_key,
                body=body,
                properties=properties,
            )

        except pika.exceptions.UnroutableError as err:
            raise err
