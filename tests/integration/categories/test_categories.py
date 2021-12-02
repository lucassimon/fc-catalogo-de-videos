import pytest

from django.urls import reverse


@pytest.mark.django_db
def test_create_a_category(api_client):
    url = reverse("categories:category-list")
    title = "Some category"
    response = api_client.post(
        url,
        data={"title": title, "description": "some category"},
        format="json",
    )
    assert response.status_code == 201
    res = response.json()

    assert title == res["title"]


@pytest.mark.django_db
def test_list_the_categories(
    api_client, category_factory, category_inactive, category_deleted
):
    categories_count = 3
    category_factory.create_batch(categories_count)

    url = reverse("categories:category-list")

    response = api_client.get(
        url,
        format="json",
    )
    assert response.status_code == 200
    res = response.json()

    assert categories_count == res["count"]


@pytest.mark.django_db
def test_get_the_category_by_id(api_client, category_factory):
    category = category_factory.create()

    url = reverse("categories:category-detail", kwargs={"pk": category.pk})

    response = api_client.get(
        url,
        format="json",
    )
    assert response.status_code == 200
    res = response.json()

    assert category.title == res["title"]


@pytest.mark.django_db
def test_update_the_category_by_id(api_client, category_factory):
    category = category_factory.create()
    new_title = "category changed"

    url = reverse("categories:category-detail", kwargs={"pk": category.pk})

    response = api_client.put(
        url,
        data={"title": new_title},
        format="json",
    )
    assert response.status_code == 200
    res = response.json()

    assert new_title == res["title"]


@pytest.mark.django_db
def test_delete_the_category_by_id(api_client, category_factory):
    category = category_factory.create()

    url = reverse("categories:category-detail", kwargs={"pk": category.pk})

    response = api_client.delete(
        url,
        format="json",
    )
    assert response.status_code == 204
