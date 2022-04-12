import factory
from faker import Factory as FakerFactory

from apps.genres import models
from tests.factories.categories import CategoryFactory

faker = FakerFactory.create()


class GenreFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Genre

    title = factory.Sequence(lambda n: "genre-%s" % n)
    description = factory.LazyAttribute(lambda _: faker.text())
    status = 1
    is_deleted = False


class GenreHasCategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.GenreHasCategory

    genre = factory.SubFactory(GenreFactory)
    category = factory.SubFactory(CategoryFactory)


class GenreWithCategoryFactory(GenreFactory):
    categories = factory.RelatedFactory(
        GenreHasCategoryFactory,
        factory_related_name="genre",
    )
