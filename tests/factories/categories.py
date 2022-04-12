import factory
from faker import Factory as FakerFactory

from apps.categories import models

faker = FakerFactory.create()


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Category

    title = factory.Sequence(lambda n: "category-%s" % n)
    description = factory.LazyAttribute(lambda _: faker.text())
    status = 1
    is_deleted = False
