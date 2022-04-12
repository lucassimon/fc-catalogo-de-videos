import pytest

from django.urls import reverse
from rest_framework import status

from apps.castmembers import models


@pytest.mark.webtest
@pytest.mark.django_db
def test_create_actor_cast_member(api_client):
    url = reverse("v1:castmembers:castmembers-list")
    name = "Some name"

    response = api_client.post(
        url,
        data={"name": name, "kind": models.CastMember.KIND_ACTOR},
        format="json",
    )

    assert response.status_code == status.HTTP_201_CREATED
    res = response.json()
    assert name == res["name"]
    assert models.CastMember.KIND_ACTOR == res["kind"]


@pytest.mark.webtest
@pytest.mark.django_db
def test_create_director_cast_member(api_client):
    url = reverse("v1:castmembers:castmembers-list")
    name = "Some name"

    response = api_client.post(
        url,
        data={"name": name, "kind": models.CastMember.KIND_DIRECTOR},
        format="json",
    )

    assert response.status_code == status.HTTP_201_CREATED
    res = response.json()
    assert name == res["name"]
    assert models.CastMember.KIND_DIRECTOR == res["kind"]
