import pytest

from django.urls import reverse
from rest_framework import status

from apps.castmembers import models


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


@pytest.mark.django_db
def test_list_the_cast_members(api_client, cast_member_factory, cast_member_deleted):
    count = 3
    cast_member_factory.create_batch(count)

    url = reverse("v1:castmembers:castmembers-list")

    response = api_client.get(
        url,
        format="json",
    )
    assert response.status_code == status.HTTP_200_OK
    res = response.json()

    assert count == res["count"]


@pytest.mark.django_db
def test_get_the_cast_member_by_id(api_client, cast_member_factory):
    obj = cast_member_factory.create()

    url = reverse("v1:castmembers:castmembers-detail", kwargs={"pk": obj.pk})

    response = api_client.get(
        url,
        format="json",
    )
    assert response.status_code == status.HTTP_200_OK
    res = response.json()

    assert obj.name == res["name"]


@pytest.mark.django_db
def test_raise_http_404_when_get_the_cast_member_is_deleted(api_client, cast_member_deleted):

    url = reverse("v1:castmembers:castmembers-detail", kwargs={"pk": cast_member_deleted.pk})

    response = api_client.get(
        url,
        format="json",
    )
    assert response.status_code == status.HTTP_404_NOT_FOUND
    res = response.json()

    assert "Not found." == res["detail"]


@pytest.mark.django_db
def test_update_the_cast_member_by_id(api_client, cast_member_factory):
    obj = cast_member_factory.create()
    new_name = "name changed"

    url = reverse("v1:castmembers:castmembers-detail", kwargs={"pk": obj.pk})

    response = api_client.put(
        url,
        data={"name": new_name},
        format="json",
    )
    assert response.status_code == status.HTTP_200_OK
    res = response.json()

    assert new_name == res["name"]


@pytest.mark.django_db
def test_delete_the_cast_member_by_id(api_client, cast_member_factory):
    obj = cast_member_factory.create()

    url = reverse("v1:castmembers:castmembers-detail", kwargs={"pk": obj.pk})

    response = api_client.delete(
        url,
        format="json",
    )
    assert response.status_code == status.HTTP_204_NO_CONTENT

    obj.refresh_from_db()
    assert obj.is_deleted == True
