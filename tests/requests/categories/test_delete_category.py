import pytest

from django.urls import reverse
from rest_framework import status


@pytest.mark.webtest
@pytest.mark.django_db
def test_delete_the_category_by_id(api_client, category_factory):
    category = category_factory.create()

    url = reverse("v1:categories:category-detail", kwargs={"pk": category.pk})

    response = api_client.delete(
        url,
        format="json",
    )
    assert response.status_code == status.HTTP_204_NO_CONTENT
