import os
import pytest
import tempfile

from django.urls import reverse

from rest_framework import status

from PIL import Image


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


def make_post_video_request(api_client, video_factory, genre_with_category_factory, tmp_file, field):
    video_data = video_factory.build()
    genre = genre_with_category_factory.create()
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


@pytest.mark.django_db
def test_create_a_simple_video(api_client, video_factory, genre_with_category_factory):
    video_data = video_factory.build()
    genre = genre_with_category_factory.create()
    category_pk = genre.categories.first().pk

    url = reverse("v1:videos:video-list")
    title = "Some item"
    response = api_client.post(
        url,
        data={
            "title": title,
            "description": "some item",
            "categories": [category_pk],
            "genres": [genre.pk],
            "year_launched": video_data.year_launched,
            "rating": video_data.rating,
            "duration": video_data.duration,
        },
        format="json",
    )

    assert response.status_code == status.HTTP_201_CREATED
    res = response.json()

    assert title == res["title"]


@pytest.mark.django_db
def test_create_a_video_with_invalid_category(
    api_client, video_factory, genre_with_category_factory, category_inactive
):

    video_data = video_factory.build()
    genre = genre_with_category_factory.create()
    category_pk = genre.categories.first().pk

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

    assert res == {"categories": ['Invalid pk "1" - object does not exist.']}


@pytest.mark.django_db
def test_create_a_video_with_deleted_genre(api_client, video_factory, genre_factory, genre_with_category_factory):

    video_data = video_factory.build()
    genre_deleted = genre_factory.create(is_deleted=True)
    genre = genre_with_category_factory.create()
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

    assert res == {"genres": ['Invalid pk "1" - object does not exist.']}


@pytest.mark.django_db
def test_create_a_video_with_genre_do_not_belongs_for_any_category(
    api_client, video_factory, genre_factory, category_factory
):
    video_data = video_factory.build()

    categories = category_factory.create_batch(3)
    genre = genre_factory.create()
    categories_pks = [categories[0].pk, categories[1].pk, categories[2].pk]

    genre = genre_factory.create()

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

    assert res == {"genres": [f"The {genre.title} genre does not belonging for any category"]}


@pytest.mark.django_db
def test_create_a_video_with_thumb_file(api_client, video_factory, genre_with_category_factory):
    tmp_file = create_temporary_image_to_upload()

    response, video_data = make_post_video_request(
        api_client, video_factory, genre_with_category_factory, tmp_file, "thumb_file"
    )

    res = response.json()

    assert response.status_code == status.HTTP_201_CREATED
    assert video_data.title == res["title"]


@pytest.mark.django_db
def test_create_a_video_with_banner_file(api_client, video_factory, genre_with_category_factory):
    tmp_file = create_temporary_image_to_upload()

    response, video_data = make_post_video_request(
        api_client, video_factory, genre_with_category_factory, tmp_file, "banner_file"
    )

    res = response.json()

    assert response.status_code == status.HTTP_201_CREATED
    assert video_data.title == res["title"]


@pytest.mark.django_db
def test_create_a_video_with_trailler_file(api_client, video_factory, genre_with_category_factory):
    tmp_file = create_temporary_video_to_upload()

    response, video_data = make_post_video_request(
        api_client, video_factory, genre_with_category_factory, tmp_file, "trailer_file"
    )

    res = response.json()

    assert response.status_code == status.HTTP_201_CREATED
    assert video_data.title == res["title"]


@pytest.mark.django_db
def test_create_a_video_with_video_file(api_client, video_factory, genre_with_category_factory):
    tmp_file = create_temporary_video_to_upload()

    response, video_data = make_post_video_request(
        api_client, video_factory, genre_with_category_factory, tmp_file, "video_file"
    )

    res = response.json()

    assert response.status_code == status.HTTP_201_CREATED
    assert video_data.title == res["title"]
