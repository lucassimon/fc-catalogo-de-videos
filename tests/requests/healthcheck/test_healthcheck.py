from django.urls import reverse

# Third
import pytest


@pytest.mark.django_db(reset_sequences=True)
@pytest.mark.parametrize(
    "language_code, language_text",
    [("es", "Hola mundo"), ("de", "Hallo Welt"), ("pt-br", "Olá mundo")],
)
def test_health_check(language_code, language_text, api_client):
    url = reverse("healthcheck")

    response = api_client.get(
        url,
        content_type="application/json",
        format="json",
        HTTP_ACCEPT_LANGUAGE=language_code,
    )
    assert response.status_code == 200
    res = response.json()
    assert language_text == res["status"]
