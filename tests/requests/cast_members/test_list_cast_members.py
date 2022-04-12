import pytest

from django.urls import reverse
from rest_framework import status


@pytest.mark.webtest
@pytest.mark.django_db
def test_list_the_cast_members(api_client, cast_member_factory):
    count = 3
    cast_member_factory.create_batch(count)

    url = reverse("v1:castmembers:castmembers-list")

    response = api_client.get(
        url,
        format="json",
    )
    assert response.status_code == status.HTTP_200_OK
    res = response.json()

    assert count == res["count"]
