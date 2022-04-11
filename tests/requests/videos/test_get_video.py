import pytest

from django.urls import reverse
from django_extensions.db.models import ActivatorModel

from rest_framework import status


@pytest.mark.django_db
def test_get_the_video_by_id(api_client, video_factory):
    obj = video_factory.create()

    url = reverse("v1:videos:video-detail", kwargs={"pk": obj.pk})

    response = api_client.get(
        url,
        format="json",
    )
    assert response.status_code == status.HTTP_200_OK
    res = response.json()

    assert obj.title == res["title"]


@pytest.mark.django_db
def test_raise_http_404_when_get_the_video_is_deleted(api_client, video_factory):
    obj = video_factory.create(is_deleted=True)

    url = reverse("v1:videos:video-detail", kwargs={"pk": obj.pk})

    response = api_client.get(
        url,
        format="json",
    )
    assert response.status_code == status.HTTP_404_NOT_FOUND
    res = response.json()

    assert "Not found." == res["detail"]


@pytest.mark.django_db
def test_raise_http_404_when_get_the_video_is_inactive(api_client, video_factory):
    obj = video_factory.create(status=ActivatorModel.INACTIVE_STATUS)

    url = reverse("v1:videos:video-detail", kwargs={"pk": obj.pk})

    response = api_client.get(
        url,
        format="json",
    )
    assert response.status_code == status.HTTP_404_NOT_FOUND
    res = response.json()

    assert "Not found." == res["detail"]
