# Third
import factory
from faker import Factory as FakerFactory
from django_extensions.db.models import ActivatorModel

# Apps
from apps.videos import models

# from django.core.files.base import ContentFile

faker = FakerFactory.create()


class VideoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Video

    title = factory.Sequence(lambda n: "video-%s" % n)
    description = factory.LazyAttribute(lambda _: faker.text())
    status = ActivatorModel.ACTIVE_STATUS
    is_deleted = False
    year_launched = factory.LazyAttribute(lambda _: int(faker.year()))
    opened = True
    rating = factory.LazyAttribute(
        lambda _: faker.random_element(
            [
                models.Video.RATING_FREE,
                models.Video.RATING_TEN_YEARS,
                models.Video.RATING_TWELVE_YEARS,
                models.Video.RATING_FOURTEEN_YEARS,
                models.Video.RATING_SIXTEEN_YEAR,
                models.Video.RATING_EIGHTEEN_YEARS,
            ]
        )
    )
    duration = factory.LazyAttribute(lambda _: faker.random_int())
    thumb_file = None
    banner_file = None
    trailer_file = None
    video_file = None

    class Params:
        with_files = factory.Trait(
            thumb_file = factory.django.ImageField(filename="thumb.png", width=200, height=200),
            banner_file = factory.django.ImageField(filename="banner.png", width=200, height=200),
            trailer_file = factory.django.FileField(filename="trailler.mp4"),
            video_file = factory.django.FileField(filename="video.mpeg"),
        )

    # factory.LazyAttribute(
    #     lambda: ContentFile(
    #         factory.django.ImageField()._make_data({"width": 1024, "height": 768}), "factory_example.jpg"
    #     )
    # )

