from django.conf import settings

# Apps
from src.core.infrastructure.rabbitmq import InterfacePublishToQueue


class PublishCreatedVideoToQueue(InterfacePublishToQueue):
    def __init__(self, rabbitmq_conn, rabbitmq_channel):
        self.conn = rabbitmq_conn
        self.channel = rabbitmq_channel
        self.exchange = settings.EXCHANGE
        self.exchange_dlx = settings.EXCHANGE_DLX
        self.queue_dl = settings.CATALOG_VIDEOS_DEAD
        self.routing_key_dl = settings.CATALOG_VIDEOS_DEAD_RK
        self.queue = settings.CATALOG_VIDEOS
        self.routing_key = settings.CATALOG_VIDEOS_RK
        self.connect()
        super().__init__()
