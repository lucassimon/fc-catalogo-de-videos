import pytest

from django.urls import reverse

from rest_framework import status


@pytest.mark.webtest
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


@pytest.mark.webtest
@pytest.mark.skip(reason="not implemented yet")
def test_list_the_videos_ordering_by_id_ascending():
    pass


@pytest.mark.webtest
@pytest.mark.skip(reason="not implemented yet")
def test_list_the_videos_ordering_by_id_descending():
    pass


@pytest.mark.webtest
@pytest.mark.skip(reason="not implemented yet")
def test_list_the_videos_search_by_title_icontains():
    pass


@pytest.mark.webtest
@pytest.mark.skip(reason="not implemented yet")
def test_list_the_videos_filter_by_status_active():
    pass


@pytest.mark.webtest
@pytest.mark.skip(reason="not implemented yet")
def test_list_the_videos_filter_by_status_inactive():
    pass


@pytest.mark.webtest
@pytest.mark.skip(reason="not implemented yet")
def test_list_the_videos_filter_by_status_is_deleted():
    pass


@pytest.mark.webtest
@pytest.mark.skip(reason="not implemented yet")
def test_list_the_videos_filter_by_status_is_not_deleted():
    pass


@pytest.mark.webtest
@pytest.mark.skip(reason="not implemented yet")
def test_list_the_videos_filter_by_opened():
    pass


@pytest.mark.webtest
@pytest.mark.skip(reason="not implemented yet")
def test_list_the_videos_filter_by_is_not_opened():
    pass
