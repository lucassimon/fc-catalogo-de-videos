# Python
import os
import tempfile
from unittest.mock import patch

from django.urls import reverse

# Third
import pytest
from PIL import Image
from rest_framework import status
from django_extensions.db.models import ActivatorModel

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

    tmp_file.write(b"foo bar")
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
        "categories": [category_pk,],
        "genres": [genre.pk.__str__()],
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
def test_create_a_simple_video(_, api_client):
    video_data = factories.VideoFactory.build()
    genre = factories.GenreWithCategoryFactory.create()
    category_pk = genre.categories.first().pk

    # apply_async_mocked.assert_called_once()

    url = reverse("v1:videos:video-list")
    title = "Some item"
    response = api_client.post(
        url,
        data={
            "title": title,
            "description": "some item",
            "categories": [category_pk],
            "genres": [genre.pk.__str__()],
            "year_launched": video_data.year_launched,
            "rating": video_data.rating,
            "duration": video_data.duration,
        },
        format="json",
    )

    assert response.status_code == status.HTTP_201_CREATED
    res = response.json()

    assert title == res["title"]


@pytest.mark.webtest
@pytest.mark.django_db(reset_sequences=True)
@patch("apps.videos.events.VideoCreated.run")
def test_create_a_video_with_invalid_category(
    _,
    api_client
):
    video_data = factories.VideoFactory.build()
    genre = factories.GenreWithCategoryFactory.create()
    category_pk = genre.categories.first().pk
    category_inactive = factories.CategoryFactory.create(status=ActivatorModel.INACTIVE_STATUS)

    url = reverse("v1:videos:video-list")
    title = "Some item"
    response = api_client.post(
        url,
        data={
            "title": title,
            "description": "some item",
            "categories": [category_pk, category_inactive.pk],
            "genres": [genre.pk],
            "year_launched": video_data.year_launched,
            "rating": video_data.rating,
            "duration": video_data.duration,
        },
        format="json",
    )

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    res = response.json()

    assert res == {'code': 400, 'name': 'Bad Request', 'description': 'Bad request syntax or unsupported method', 'errors': {'categories': [f'Invalid pk "{category_inactive.pk}" - object does not exist.']}, 'exception': 'ValidationError'}


@pytest.mark.webtest
@pytest.mark.django_db(reset_sequences=True)
@patch("apps.videos.events.VideoCreated.run")
def test_create_a_video_with_deleted_genre(_, api_client):

    video_data = factories.VideoFactory.build()
    genre_deleted = factories.GenreFactory.create(is_deleted=True)
    genre = factories.GenreWithCategoryFactory.create()
    category_pk = genre.categories.first().pk

    url = reverse("v1:videos:video-list")
    title = "Some item"
    response = api_client.post(
        url,
        data={
            "title": title,
            "description": "some item",
            "categories": [category_pk],
            "genres": [genre.pk, genre_deleted.pk],
            "year_launched": video_data.year_launched,
            "rating": video_data.rating,
            "duration": video_data.duration,
        },
        format="json",
    )

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    res = response.json()

    assert res == {'code': 400, 'name': 'Bad Request', 'description': 'Bad request syntax or unsupported method', 'errors': {'genres': [f'Invalid pk "{genre_deleted.pk}" - object does not exist.']}, 'exception': 'ValidationError'}


@pytest.mark.webtest
@pytest.mark.django_db(reset_sequences=True)
@patch("apps.videos.events.VideoCreated.run")
def test_create_a_video_with_genre_do_not_belongs_for_any_category(
    _,
    api_client
):
    video_data = factories.VideoFactory.build()

    categories = factories.CategoryFactory.create_batch(3)
    genre = factories.GenreFactory.create()
    categories_pks = [categories[0].pk, categories[1].pk, categories[2].pk]

    url = reverse("v1:videos:video-list")
    title = "Some item"
    response = api_client.post(
        url,
        data={
            "title": title,
            "description": "some item",
            "categories": categories_pks,
            "genres": [genre.pk],
            "year_launched": video_data.year_launched,
            "rating": video_data.rating,
            "duration": video_data.duration,
        },
        format="json",
    )

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    res = response.json()

    assert res == {'code': 400, 'name': 'Bad Request', 'description': 'Bad request syntax or unsupported method', 'errors': {'genres': [f'The {genre.title} genre does not belonging for any category']}, 'exception': 'ValidationError'}


@pytest.mark.webtest
@pytest.mark.django_db(reset_sequences=True)
@patch("apps.videos.events.VideoCreated.run")
def test_create_a_video_with_thumb_file(_, api_client):
    tmp_file = create_temporary_image_to_upload()

    response, video_data = make_post_video_request(
        api_client, tmp_file, "thumb_file"
    )

    res = response.json()

    assert response.status_code == status.HTTP_201_CREATED
    assert video_data.title == res["title"]


@pytest.mark.webtest
@pytest.mark.django_db(reset_sequences=True)
@patch("apps.videos.events.VideoCreated.run")
def test_create_a_video_with_banner_file(_, api_client):
    tmp_file = create_temporary_image_to_upload()

    response, video_data = make_post_video_request(
        api_client, tmp_file, "banner_file"
    )

    res = response.json()

    assert response.status_code == status.HTTP_201_CREATED
    assert video_data.title == res["title"]


@pytest.mark.webtest
@pytest.mark.django_db(reset_sequences=True)
@patch("apps.videos.events.VideoCreated.run")
def test_create_a_video_with_trailler_file(_, api_client):
    tmp_file = create_temporary_video_to_upload()

    response, video_data = make_post_video_request(
        api_client, tmp_file, "trailer_file"
    )

    res = response.json()

    assert response.status_code == status.HTTP_201_CREATED
    assert video_data.title == res["title"]


@pytest.mark.webtest
@pytest.mark.django_db(reset_sequences=True)
@patch("apps.videos.events.VideoCreated.run")
def test_create_a_video_with_video_file(_, api_client):
    tmp_file = create_temporary_video_to_upload()

    response, video_data = make_post_video_request(
        api_client, tmp_file, "video_file"
    )

    res = response.json()

    assert response.status_code == status.HTTP_201_CREATED
    assert video_data.title == res["title"]
