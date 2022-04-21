import pytest

from django.urls import reverse
from rest_framework import status

from tests import factories

@pytest.mark.webtest
@pytest.mark.django_db(reset_sequences=True)
def test_delete_the_genre_by_id(api_client):
    obj = factories.GenreFactory.create()

    url = reverse("v1:genres:genre-detail", kwargs={"pk": obj.pk})

    response = api_client.delete(
        url,
        format="json",
    )
    assert response.status_code == status.HTTP_204_NO_CONTENT

    obj.refresh_from_db()
    assert obj.is_deleted == True
