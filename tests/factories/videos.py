import factory
from faker import Factory as FakerFactory

from apps.videos import models
from django_extensions.db.models import ActivatorModel
from django.core.files.base import ContentFile

faker = FakerFactory.create()


class VideoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Video

    title = factory.LazyAttribute(lambda x: faker.sentence(nb_words=4))
    description = factory.LazyAttribute(lambda x: faker.text())
    status = ActivatorModel.ACTIVE_STATUS
    is_deleted = False
    year_launched = factory.LazyAttribute(lambda x: int(faker.year()))
    opened = True
    rating = factory.LazyAttribute(
        lambda x: faker.random_element(
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
    duration = factory.LazyAttribute(lambda x: faker.random_int())
    thumb_file = factory.LazyAttribute(
        lambda _: ContentFile(factory.django.ImageField()._make_data({"width": 1024, "height": 768}), "example.jpg")
    )
