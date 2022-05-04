from django.urls import reverse

# Third
import ipdb
import pytest
from devtools import debug as dev_debug
from rest_framework import status
from django_extensions.db.models import ActivatorModel

# Apps
from tests import factories
from apps.videos import models


def make_videos():
    common_video = factories.VideoFactory.create(rating=models.Video.RATING_FREE, status=ActivatorModel.ACTIVE_STATUS)
    video_inactive = factories.VideoFactory.create(rating=models.Video.RATING_FREE, status=ActivatorModel.INACTIVE_STATUS, is_deleted=False)
    video_deleted = factories.VideoFactory.create(rating=models.Video.RATING_FREE, status=ActivatorModel.ACTIVE_STATUS, is_deleted=True)
    video_not_opened = factories.VideoFactory.create(rating=models.Video.RATING_FREE, status=ActivatorModel.ACTIVE_STATUS, opened=False)

    return common_video, video_inactive, video_deleted, video_not_opened



@pytest.mark.webtest
@pytest.mark.django_db(reset_sequences=True)
def test_list_the_videos(api_client):
    make_videos()

    url = reverse("v1:videos:video-list")

    response = api_client.get(
        url,
        format="json",
    )
    assert response.status_code == status.HTTP_200_OK
    res = response.json()

    assert 4 == res["count"]


@pytest.mark.webtest
@pytest.mark.django_db(reset_sequences=True)
def test_list_the_videos_ordering_by_id_ascending(api_client):
    make_videos()

    url = reverse("v1:videos:video-list")
    url =f"{url}?ordering=id"

    response = api_client.get(
        url,
        format="json",
    )
    res = response.json()

    assert response.status_code == status.HTTP_200_OK
    assert 4 == res["count"]



@pytest.mark.webtest
@pytest.mark.django_db(reset_sequences=True)
def test_list_the_videos_ordering_by_id_descending(api_client):
    make_videos()

    url = reverse("v1:videos:video-list")
    url =f"{url}?ordering=-id"

    response = api_client.get(
        url,
        format="json",
    )
    res = response.json()

    assert response.status_code == status.HTTP_200_OK
    assert 4 == res["count"]


@pytest.mark.webtest
@pytest.mark.django_db(reset_sequences=True)
def test_list_the_videos_search_by_title_icontains(api_client):
    make_videos()
    factories.VideoFactory.create(title="Some strange title ")

    url = reverse("v1:videos:video-list")
    url =f"{url}?search=strange"

    response = api_client.get(
        url,
        format="json",
    )
    res = response.json()

    assert response.status_code == status.HTTP_200_OK
    assert 1 == res["count"]



@pytest.mark.webtest
@pytest.mark.django_db(reset_sequences=True)
def test_list_the_videos_filter_by_status_active(api_client):
    make_videos()

    url = reverse("v1:videos:video-list")
    url =f"{url}?status={ActivatorModel.ACTIVE_STATUS}"

    response = api_client.get(
        url,
        format="json",
    )
    res = response.json()

    assert response.status_code == status.HTTP_200_OK
    assert 3 == res["count"]


@pytest.mark.webtest
@pytest.mark.django_db(reset_sequences=True)
def test_list_the_videos_filter_by_status_inactive(api_client):
    make_videos()

    url = reverse("v1:videos:video-list")
    url =f"{url}?status={ActivatorModel.INACTIVE_STATUS}"

    response = api_client.get(
        url,
        format="json",
    )
    res = response.json()

    assert response.status_code == status.HTTP_200_OK
    assert 1 == res["count"]


@pytest.mark.webtest
@pytest.mark.django_db(reset_sequences=True)
def test_list_the_videos_filter_by_is_deleted(api_client):
    make_videos()

    url = reverse("v1:videos:video-list")
    url =f"{url}?is_deleted=true"

    response = api_client.get(
        url,
        format="json",
    )
    res = response.json()

    assert response.status_code == status.HTTP_200_OK
    assert 1 == res["count"]


@pytest.mark.webtest
@pytest.mark.django_db(reset_sequences=True)
def test_list_the_videos_filter_by_is_not_deleted(api_client):
    make_videos()

    url = reverse("v1:videos:video-list")
    url =f"{url}?is_deleted=false"

    response = api_client.get(
        url,
        format="json",
    )
    res = response.json()

    assert response.status_code == status.HTTP_200_OK
    assert 3 == res["count"]


@pytest.mark.webtest
@pytest.mark.django_db(reset_sequences=True)
def test_list_the_videos_filter_by_opened(api_client):
    make_videos()

    url = reverse("v1:videos:video-list")
    url =f"{url}?opened=true"

    response = api_client.get(
        url,
        format="json",
    )
    res = response.json()

    assert response.status_code == status.HTTP_200_OK
    assert 3 == res["count"]


@pytest.mark.webtest
@pytest.mark.django_db(reset_sequences=True)
def test_list_the_videos_filter_by_is_not_opened(api_client):
    make_videos()

    url = reverse("v1:videos:video-list")
    url =f"{url}?opened=false"

    response = api_client.get(
        url,
        format="json",
    )
    res = response.json()

    assert response.status_code == status.HTTP_200_OK
    assert 1 == res["count"]



@pytest.mark.webtest
@pytest.mark.django_db(reset_sequences=True)
def test_list_the_videos_filter_by_rating(api_client):
    make_videos()
    factories.VideoFactory.create(rating=models.Video.RATING_TEN_YEARS)
    factories.VideoFactory.create(rating=models.Video.RATING_TEN_YEARS)

    url = reverse("v1:videos:video-list")
    url =f"{url}?rating={models.Video.RATING_TEN_YEARS}"

    response = api_client.get(
        url,
        format="json",
    )
    res = response.json()

    assert response.status_code == status.HTTP_200_OK
    assert 2 == res["count"]


@pytest.mark.skip("Not implemented yet")
def test_list_the_videos_filter_by_year_launched():
    pass
