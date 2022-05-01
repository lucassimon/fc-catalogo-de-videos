# Third
from celery import shared_task
from celery.utils.log import get_task_logger
from django_extensions.db.models import ActivatorModel

# Apps
from src.core.infrastructure.rabbitmq import RabbitMQ
from src.videos.infrastructure.publish_video_to_queue import PublishCreatedVideoToQueue

# circular imports
# from apps.videos.models import Video as VideoModel


logger = get_task_logger(__name__)


class VideoTasks:

    @classmethod
    def make_message(cls, video, action="created"):
        return {
            "action": action,
            "video": {
                "id": f"{video.id}",
                "thumb_file": video.thumb_file.url,
                "banner_file": video.banner_file.url,
                "trailer_file": video.trailer_file.url,
                "video_file": video.video_file.url,
            }
        }

    @shared_task
    def send_message_to_created_video_queue(video):
        logger.info("Start send message")

        if video.is_deleted is True:
            raise Exception("Video created with deleted attribute")

        if video.status == ActivatorModel.INACTIVE_STATUS:
            raise Exception("Video created with inactive status")

        if bool(video.trailer_file) is False or bool(video.video_file) is False:
            raise Exception("Trailer or original file was not uploaded")


        message = VideoTasks.make_message(video)

        #  Create a connection with pika
        rabbitmq_conn, rabbitmq_channel = RabbitMQ.connect()
        prepare_to_send = PublishCreatedVideoToQueue(rabbitmq_conn, rabbitmq_channel)
        # Publish a message as a json
        prepare_to_send.run(message)
