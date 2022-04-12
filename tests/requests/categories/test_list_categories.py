import pytest

from django.urls import reverse
from rest_framework import status


@pytest.mark.webtest
@pytest.mark.django_db
def test_list_the_categories(api_client, category_factory):
    categories_count = 3
    category_factory.create_batch(categories_count)

    url = reverse("v1:categories:category-list")

    response = api_client.get(
        url,
        format="json",
    )
    assert response.status_code == status.HTTP_200_OK
    res = response.json()

    assert categories_count == res["count"]
