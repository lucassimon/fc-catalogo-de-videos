import pytest

from django.urls import reverse
from rest_framework import status


@pytest.mark.webtest
@pytest.mark.django_db
def test_update_the_cast_member_by_id(api_client, cast_member_factory):
    obj = cast_member_factory.create()
    new_name = "name changed"

    url = reverse("v1:castmembers:castmembers-detail", kwargs={"pk": obj.pk})

    response = api_client.put(
        url,
        data={"name": new_name},
        format="json",
    )
    assert response.status_code == status.HTTP_200_OK
    res = response.json()

    assert new_name == res["name"]
