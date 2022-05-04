# Python
import os
import tempfile
from unittest.mock import patch

from django.urls import reverse

# Third
import pytest
from PIL import Image
from rest_framework import status

# Apps
from tests import factories


def create_temporary_image_to_upload():
    image = Image.new("RGB", (100, 100))
    tmp_file = tempfile.NamedTemporaryFile(suffix=".jpg")
    image.save(tmp_file, format="JPEG")
    tmp_file.seek(0)

    return tmp_file


def create_temporary_video_to_upload():
    tmp_file = tempfile.NamedTemporaryFile(suffix=".mpeg")
    tmp_file.seek(0)
    return tmp_file


def make_post_video_request(api_client, tmp_file, field):
    video_data = factories.VideoFactory.build()
    genre = factories.GenreWithCategoryFactory.create()
    category_pk = genre.categories.first().pk
    url = reverse("v1:videos:video-list")

    data = {
        "title": video_data.title,
        "description": "some item",
        "categories": [category_pk],
        "genres": [genre.pk],
        "year_launched": video_data.year_launched,
        "rating": video_data.rating,
        "duration": video_data.duration,
    }

    data[field] = tmp_file

    response = api_client.post(
        url,
        data=data,
        format="multipart",
    )

    return response, video_data


@pytest.mark.webtest
@pytest.mark.django_db(reset_sequences=True)
@patch("apps.videos.events.VideoCreated.run")
def test_update_the_video_by_id(_, api_client):
    obj = factories.VideoFactory.create()
    new_title = "item changed"

    url = reverse("v1:videos:video-detail", kwargs={"pk": obj.pk})

    response = api_client.patch(
        url,
        data={"title": new_title},
        format="json",
    )
    assert response.status_code == status.HTTP_200_OK
    res = response.json()

    assert new_title == res["title"]


@pytest.mark.webtest
@pytest.mark.django_db(reset_sequences=True)
@patch("apps.videos.events.VideoCreated.run")
def test_update_a_video_with_thumb_file(_, api_client):
    video = factories.VideoFactory.create()
    url = reverse("v1:videos:video-detail", kwargs={"pk": video.pk})

    updated_tmp_file = create_temporary_image_to_upload()
    expected_updated_tmp_file = os.path.basename(updated_tmp_file.name)

    response = api_client.put(
        url,
        data={
            "thumb_file": updated_tmp_file,
        },
        format="multipart",
    )

    response_json = response.json()
    filename = os.path.basename(response_json["thumb_file"])

    assert response.status_code == status.HTTP_200_OK
    assert filename == expected_updated_tmp_file
