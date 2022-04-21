import pytest

from django.urls import reverse

from rest_framework import status


@pytest.mark.webtest
@pytest.mark.django_db(reset_sequences=True)
def test_create_a_category(api_client):
    url = reverse("v1:categories:category-list")
    title = "Some category"
    response = api_client.post(
        url,
        data={"title": title, "description": "some category"},
        format="json",
    )
    assert response.status_code == status.HTTP_201_CREATED
    res = response.json()

    assert title == res["title"]
