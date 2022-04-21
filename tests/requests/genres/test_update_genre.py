import pytest

from django.urls import reverse
from rest_framework import status

from tests import factories

@pytest.mark.webtest
@pytest.mark.django_db(reset_sequences=True)
def test_update_the_genre_by_id(api_client):
    obj = factories.GenreFactory.create()
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
