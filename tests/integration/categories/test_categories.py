import pytest

from django.urls import reverse
from django_extensions.db.models import ActivatorModel
from rest_framework import status


@pytest.mark.django_db
def test_create_a_category(api_client):
    url = reverse("v1:categories:category-list")
    title = "Some category"
    response = api_client.post(
        url,
        data={"title": title, "description": "some category"},
        format="json",
    )
    assert response.status_code == status.HTTP_201_CREATED
    res = response.json()

    assert title == res["title"]


@pytest.mark.django_db
def test_list_the_categories(
    api_client, category_factory, category_inactive, category_deleted
):
    categories_count = 3
    category_factory.create_batch(categories_count)

    url = reverse("v1:categories:category-list")

    response = api_client.get(
        url,
        format="json",
    )
    assert response.status_code == status.HTTP_200_OK
    res = response.json()

    assert categories_count == res["count"]


@pytest.mark.django_db
def test_get_the_category_by_id(api_client, category_factory):
    category = category_factory.create()

    url = reverse("v1:categories:category-detail", kwargs={"pk": category.pk})

    response = api_client.get(
        url,
        format="json",
    )
    assert response.status_code == status.HTTP_200_OK
    res = response.json()

    assert category.title == res["title"]


@pytest.mark.django_db
def test_raise_http_404_when_get_the_category_is_deleted(api_client, category_factory):
    category = category_factory.create(is_deleted=True)

    url = reverse("v1:categories:category-detail", kwargs={"pk": category.pk})

    response = api_client.get(
        url,
        format="json",
    )
    assert response.status_code == status.HTTP_404_NOT_FOUND
    res = response.json()

    assert "Not found." == res["detail"]


@pytest.mark.django_db
def test_raise_http_404_when_get_the_category_is_inactive(api_client, category_factory):
    category = category_factory.create(status=ActivatorModel.INACTIVE_STATUS)

    url = reverse("v1:categories:category-detail", kwargs={"pk": category.pk})

    response = api_client.get(
        url,
        format="json",
    )
    assert response.status_code == status.HTTP_404_NOT_FOUND
    res = response.json()

    assert "Not found." == res["detail"]


@pytest.mark.django_db
def test_update_the_category_by_id(api_client, category_factory):
    category = category_factory.create()
    new_title = "category changed"

    url = reverse("v1:categories:category-detail", kwargs={"pk": category.pk})

    response = api_client.put(
        url,
        data={"title": new_title},
        format="json",
    )
    assert response.status_code == status.HTTP_200_OK
    res = response.json()

    assert new_title == res["title"]


@pytest.mark.django_db
def test_delete_the_category_by_id(api_client, category_factory):
    category = category_factory.create()

    url = reverse("v1:categories:category-detail", kwargs={"pk": category.pk})

    response = api_client.delete(
        url,
        format="json",
    )
    assert response.status_code == status.HTTP_204_NO_CONTENT
