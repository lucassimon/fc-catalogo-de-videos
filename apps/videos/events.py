# Third
from django_extensions.db.models import ActivatorModel

# Apps
from apps.videos.tasks import celery_send_message_to_created_video_queue


class VideoCreatedTrailerFileTasks:

    def make_message(self, video, action="created"):
        return {
            "action": action,
            "field": "trailer_file",
            "video": {
                "id": f"{video.id}",
                "trailer_file": video.trailer_file.url,
            }
        }

    def send(self, video):

        # se nao existir eu nao envio a mensagem
        if bool(video.trailer_file) is False:
            return

        message = self.make_message(video)

        celery_send_message_to_created_video_queue(message)



class VideoCreatedVideoFileTasks:

    def make_message(self, video, action="created"):
        return {
            "action": action,
            "field": "video_file",
            "video": {
                "id": f"{video.id}",
                "video_file": video.video_file.url,
            }
        }

    def send(self, video):

        # se nao existir eu nao envio a mensagem
        if bool(video.video_file) is False:
            return

        message = self.make_message(video)

        celery_send_message_to_created_video_queue(message)


class VideoCreated:

    def __init__(self, video_pk):

        # circular imports
        # Não entendi pois nao estou referenciando tasks no modelo
        # Apps
        from apps.videos.models import Video as VideoModel

        video = VideoModel.objects.get(id=video_pk)

        if video.is_deleted is True:
            raise Exception("Video created with deleted attribute")

        if video.status == ActivatorModel.INACTIVE_STATUS:
            raise Exception("Video created with inactive status")

        self.video = video

    def run(self):
        VideoCreatedVideoFileTasks().send(self.video)
        VideoCreatedTrailerFileTasks().send(self.video)

