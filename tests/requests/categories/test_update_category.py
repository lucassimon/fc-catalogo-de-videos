import pytest

from django.urls import reverse
from rest_framework import status


@pytest.mark.webtest
@pytest.mark.django_db
def test_update_the_category_by_id(api_client, category_factory):
    category = category_factory.create()
    new_title = "category changed"

    url = reverse("v1:categories:category-detail", kwargs={"pk": category.pk})

    response = api_client.put(
        url,
        data={"title": new_title},
        format="json",
    )
    assert response.status_code == status.HTTP_200_OK
    res = response.json()

    assert new_title == res["title"]
