import factory
from faker import Factory as FakerFactory

from apps.categories import models

faker = FakerFactory.create()


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Category

    title = factory.LazyAttribute(lambda x: faker.sentence(nb_words=4))
    description = factory.LazyAttribute(lambda x: faker.text())
    status = 1
    is_deleted = False
