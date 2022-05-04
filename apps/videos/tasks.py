# Third
from celery import shared_task
from celery.utils.log import get_task_logger

# Apps
from src.core.infrastructure.rabbitmq import RabbitMQ
from src.videos.infrastructure.publish_video_to_queue import PublishCreatedVideoToQueue

logger = get_task_logger(__name__)


@shared_task
def celery_send_message_to_created_video_queue(message):
    logger.info("Start send message")

    # Third
    logger.info(f"message: {message}")
    #  Create a connection with pika
    rabbitmq_conn, rabbitmq_channel = RabbitMQ.connect()

    prepare_to_send = PublishCreatedVideoToQueue(rabbitmq_conn, rabbitmq_channel)

    # Publish a message as a json
    prepare_to_send.run(message)
