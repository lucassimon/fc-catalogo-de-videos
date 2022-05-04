from django.urls import reverse

# Third
import pytest
from rest_framework import status

# Apps
from tests.factories import categories as factories


@pytest.mark.webtest
@pytest.mark.django_db(reset_sequences=True)
def test_list_the_categories(api_client):
    categories_count = 3
    factories.CategoryFactory.create_batch(categories_count)

    url = reverse("v1:categories:category-list")

    response = api_client.get(
        url,
        format="json",
    )
    assert response.status_code == status.HTTP_200_OK
    res = response.json()

    assert categories_count == res["count"]
