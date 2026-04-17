import pytest
from django.test import Client


@pytest.fixture
def client():
    return Client()


@pytest.mark.django_db
def test_home_get_request(client):
    response = client.get("/home")
    assert response is not None


@pytest.mark.django_db
def test_home_status_code(client):
    response = client.get("/home")
    assert response.status_code == 200


@pytest.mark.django_db
def test_home_content(client):
    response = client.get("/home")
    assert b"Hello World" in response.content
