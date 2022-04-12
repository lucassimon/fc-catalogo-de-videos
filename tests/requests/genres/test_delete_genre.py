import pytest

from django.urls import reverse
from rest_framework import status


@pytest.mark.webtest
@pytest.mark.django_db
def test_delete_the_genre_by_id(api_client, genre_factory):
    obj = genre_factory.create()

    url = reverse("v1:genres:genre-detail", kwargs={"pk": obj.pk})

    response = api_client.delete(
        url,
        format="json",
    )
    assert response.status_code == status.HTTP_204_NO_CONTENT

    obj.refresh_from_db()
    assert obj.is_deleted == True
