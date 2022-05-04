from django.urls import reverse

# Third
import pytest
from rest_framework import status

# Apps
from tests import factories


@pytest.mark.webtest
@pytest.mark.django_db(reset_sequences=True)
def test_delete_the_video_by_id(api_client):
    obj = factories.VideoFactory.create()

    url = reverse("v1:videos:video-detail", kwargs={"pk": obj.pk})

    response = api_client.delete(
        url,
        format="json",
    )
    assert response.status_code == status.HTTP_204_NO_CONTENT

    obj.refresh_from_db()
    assert obj.is_deleted == True
