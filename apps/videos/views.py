from django.db import IntegrityError, transaction

# Third
from rest_framework import serializers

# Apps
from apps.videos import events


def thumb_upload_to_path(instance, filename):
    return f"catalago-de-videos/{instance.id.__str__()}/thumb/{filename}"


def banner_upload_to_path(instance, filename):
    return f"catalago-de-videos/{instance.id.__str__()}/banner/{filename}"


def trailer_upload_to_path(instance, filename):
    return f"catalago-de-videos/{instance.id.__str__()}/trailer/{filename}"


def video_upload_to_path(instance, filename):
    return f"catalago-de-videos/{instance.id.__str__()}/videos/{filename}"


def create_video(serializer: serializers.Serializer):
    # https://github.com/codeedu/laravel-microservice-quickstart/blob/a5bc980b97e93cf35561af0b8c197490a92d990d/app/Models/Traits/UploadFiles.php
    try:
        with transaction.atomic():
            instance = serializer.save()

        # tasks.VideoTasks.send_message_to_created_video_queue.apply_async((instance.id.__str__(),),)
        task = events.VideoCreated(instance.id.__str__())
        task.run()

        return instance

    except IntegrityError:
        delete_files(instance)
        transaction.rollback()
        return None


def update_video():
    raise NotImplementedError()


def delete_video(instance):
    instance.soft_delete()


def delete_old_files():
    raise NotImplementedError()


def delete_files(instance):
    for file in [
        instance.thumb_file,
        instance.banner_file,
        instance.trailler_file,
        instance.video_file,
    ]:
        delete_file(file)


def delete_file(file):
    raise NotImplementedError()
