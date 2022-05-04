from django.urls import reverse

# Third
import pytest
from rest_framework import status

# Apps
from tests import factories


@pytest.mark.webtest
@pytest.mark.django_db(reset_sequences=True)
def test_list_the_genres(api_client):
    count = 3
    factories.GenreFactory.create_batch(count)

    url = reverse("v1:genres:genre-list")

    response = api_client.get(
        url,
        format="json",
    )
    assert response.status_code == status.HTTP_200_OK
    res = response.json()

    assert count == res["count"]
