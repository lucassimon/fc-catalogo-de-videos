import pytest

from django.urls import reverse

from rest_framework import status


@pytest.mark.django_db
def test_list_the_videos(api_client, video_factory):
    count = 3
    video_factory.create_batch(count)

    url = reverse("v1:videos:video-list")

    response = api_client.get(
        url,
        format="json",
    )
    assert response.status_code == status.HTTP_200_OK
    res = response.json()

    assert count == res["count"]
