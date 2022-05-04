from django.urls import reverse

# Third
import pytest
from rest_framework import status

# Apps
from tests import factories


@pytest.mark.webtest
@pytest.mark.django_db(reset_sequences=True)
def test_get_the_genre_by_id(api_client):
    obj = factories.GenreFactory.create()

    url = reverse("v1:genres:genre-detail", kwargs={"pk": obj.pk})

    response = api_client.get(
        url,
        format="json",
    )
    assert response.status_code == status.HTTP_200_OK
    res = response.json()

    assert obj.title == res["title"]


@pytest.mark.webtest
@pytest.mark.django_db(reset_sequences=True)
def test_raise_http_404_when_get_the_genre_that_does_not_exists(api_client):

    url = reverse("v1:genres:genre-detail", kwargs={"pk": 99})

    response = api_client.get(
        url,
        format="json",
    )
    assert response.status_code == status.HTTP_404_NOT_FOUND
    res = response.json()

    assert "Not found." == res["detail"]
