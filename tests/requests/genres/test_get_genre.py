import pytest

from django.urls import reverse
from rest_framework import status


@pytest.mark.webtest
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


@pytest.mark.webtest
@pytest.mark.django_db
def test_raise_http_404_when_get_the_genre_that_does_not_exists(api_client):

    url = reverse("v1:genres:genre-detail", kwargs={"pk": 99})

    response = api_client.get(
        url,
        format="json",
    )
    assert response.status_code == status.HTTP_404_NOT_FOUND
    res = response.json()

    assert "Not found." == res["detail"]