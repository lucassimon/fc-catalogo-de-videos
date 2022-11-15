# Third
from django_extensions.db.models import ActivatorModel, TimeStampedModel, TitleSlugDescriptionModel

# Apps
from apps.core.models import UUIDModel, SoftDeleteModel
from apps.core.managers import SoftDeleteAndInactiveManager
from apps.core.messages import CATEGORY as CATEGORY_TEXT
from apps.core.messages import CATEGORIES

# from django.db.models.signals import post_save
# from django.dispatch import receiver


# from main.celery import rabbitmq_producer


class Category(
    TitleSlugDescriptionModel,
    UUIDModel,
    ActivatorModel,
    SoftDeleteModel,
    TimeStampedModel,
):

    objects = SoftDeleteAndInactiveManager()

    def __str__(self):
        return f"{self.title}"

    class Meta:
        ordering = ["created"]
        verbose_name = CATEGORY_TEXT
        verbose_name_plural = CATEGORIES


# @receiver(post_save, sender=Category)
# def category_sync(instance, created, **kwargs):
#     action = "created" if created else "updated"
#     routing_key = f"model.category.{action}"
#     with rabbitmq_producer() as producer:
#         producer.publish(body={"id": instance.id, "name": instance.name}, routing_key=routing_key, exchange="amq.topic")
