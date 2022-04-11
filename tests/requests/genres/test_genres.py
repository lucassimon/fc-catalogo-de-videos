import pytest

from django.urls import reverse
from django_extensions.db.models import ActivatorModel
from rest_framework import status


@pytest.mark.django_db
def test_create_a_genre(api_client, category_factory):
    category = category_factory.create()
    url = reverse("v1:genres:genre-list")
    title = "Some item"
    response = api_client.post(
        url,
        data={"categories": [category.pk], "title": title, "description": "some item"},
        format="json",
    )
    assert response.status_code == status.HTTP_201_CREATED
    res = response.json()

    assert title == res["title"]


@pytest.mark.django_db
def test_list_the_genres(api_client, genre_factory):
    count = 3
    genre_factory.create_batch(count)

    url = reverse("v1:genres:genre-list")

    response = api_client.get(
        url,
        format="json",
    )
    assert response.status_code == status.HTTP_200_OK
    res = response.json()

    assert count == res["count"]


@pytest.mark.django_db
def test_get_the_genre_by_id(api_client, genre_factory):
    obj = genre_factory.create()

    url = reverse("v1:genres:genre-detail", kwargs={"pk": obj.pk})

    response = api_client.get(
        url,
        format="json",
    )
    assert response.status_code == status.HTTP_200_OK
    res = response.json()

    assert obj.title == res["title"]


@pytest.mark.django_db
def test_raise_http_404_when_get_the_genre_is_deleted(api_client, genre_factory):
    obj = genre_factory.create(is_deleted=True)

    url = reverse("v1:genres:genre-detail", kwargs={"pk": obj.pk})

    response = api_client.get(
        url,
        format="json",
    )
    assert response.status_code == status.HTTP_404_NOT_FOUND
    res = response.json()

    assert "Not found." == res["detail"]


@pytest.mark.django_db
def test_raise_http_404_when_get_the_genre_is_inactive(api_client, genre_factory):
    obj = genre_factory.create(status=ActivatorModel.INACTIVE_STATUS)

    url = reverse("v1:genres:genre-detail", kwargs={"pk": obj.pk})

    response = api_client.get(
        url,
        format="json",
    )
    assert response.status_code == status.HTTP_404_NOT_FOUND
    res = response.json()

    assert "Not found." == res["detail"]


@pytest.mark.django_db
def test_update_the_genre_by_id(api_client, genre_factory):
    obj = genre_factory.create()
    new_title = "item changed"

    url = reverse("v1:genres:genre-detail", kwargs={"pk": obj.pk})

    response = api_client.patch(
        url,
        data={"title": new_title},
        format="json",
    )
    assert response.status_code == status.HTTP_200_OK
    res = response.json()

    assert new_title == res["title"]


@pytest.mark.django_db
def test_delete_the_genre_by_id(api_client, genre_factory):
    obj = genre_factory.create()

    url = reverse("v1:genres:genre-detail", kwargs={"pk": obj.pk})

    response = api_client.delete(
        url,
        format="json",
    )
    assert response.status_code == status.HTTP_204_NO_CONTENT

    obj.refresh_from_db()
    assert obj.is_deleted == True
