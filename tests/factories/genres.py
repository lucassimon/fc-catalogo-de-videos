import factory
from faker import Factory as FakerFactory

from apps.genres import models
from tests.factories.categories import CategoryFactory

faker = FakerFactory.create()


class GenreFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Genre

    category = factory.SubFactory(CategoryFactory)
    title = factory.LazyAttribute(lambda x: faker.sentence(nb_words=4))
    description = factory.LazyAttribute(lambda x: faker.text())
    status = 1
    is_deleted = False
