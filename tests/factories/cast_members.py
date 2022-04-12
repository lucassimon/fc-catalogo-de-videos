import factory
from faker import Factory as FakerFactory

from apps.castmembers import models


faker = FakerFactory.create()


class CastMemberFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.CastMember

    name = factory.Sequence(lambda n: "member-%s" % n)
    kind = models.CastMember.KIND_ACTOR
    is_deleted = False
