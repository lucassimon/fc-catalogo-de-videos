import factory
from faker import Factory as FakerFactory

from apps.categories.models import Category
from apps.genres import models
from tests.factories.categories import CategoryFactory

faker = FakerFactory.create()


class GenreFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Genre

    title = factory.LazyAttribute(lambda x: faker.sentence(nb_words=4))
    description = factory.LazyAttribute(lambda x: faker.text())
    status = 1
    is_deleted = False

    @factory.post_generation
    def categories(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for item in extracted:
                if isinstance(item, Category):
                    self.categories.add(item)
