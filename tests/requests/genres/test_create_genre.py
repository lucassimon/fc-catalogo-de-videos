import pytest

from django.urls import reverse
from rest_framework import status

from tests.factories import categories as factories


@pytest.mark.webtest
@pytest.mark.django_db(reset_sequences=True)
def test_create_a_genre(api_client):
    category = factories.CategoryFactory.create()
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
