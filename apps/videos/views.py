from django.db import IntegrityError, transaction

# Third
from rest_framework import serializers

# Apps
from apps.videos import tasks


def thumb_upload_to_path(instance, filename):
    return "catalago-de-videos/{0}/thumb/{1}".format(instance.id.__str__(), filename)


def banner_upload_to_path(instance, filename):
    return "catalago-de-videos/{0}/banner/{1}".format(instance.id.__str__(), filename)


def trailer_upload_to_path(instance, filename):
    return "catalago-de-videos/{0}/trailer/{1}".format(instance.id.__str__(), filename)


def video_upload_to_path(instance, filename):
    return "catalago-de-videos/{0}/videos/{1}".format(instance.id.__str__(), filename)


def create_video(serializer: serializers.Serializer):
    # https://github.com/codeedu/laravel-microservice-quickstart/blob/a5bc980b97e93cf35561af0b8c197490a92d990d/app/Models/Traits/UploadFiles.php
    try:
        with transaction.atomic():
            instance = serializer.save()

        tasks.VideoTasks.send_message_to_created_video_queue.apply_async((instance,),)

        return instance

    except IntegrityError:
        delete_files(instance)
        transaction.rollback()


def update_video(serializer: serializers.Serializer):
    pass


def delete_video(instance):
    instance.soft_delete()


def delete_old_files(instance):
    pass


def delete_files(instance):
    for file in [
        instance.thumb_file,
        instance.banner_file,
        instance.trailler_file,
        instance.video_file,
    ]:
        deleteFile(file)


def deleteFile(file):
    pass
