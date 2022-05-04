from django.urls import reverse

# Third
import pytest
from rest_framework import status

# Apps
from tests import factories


@pytest.mark.webtest
@pytest.mark.django_db(reset_sequences=True)
def test_update_the_cast_member_by_id(api_client):
    obj = factories.CastMemberFactory.create()
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
