import pytest
from django.test import Client as TestClient
from company.models import Service

@pytest.fixture
def client():
    return TestClient()

@pytest.mark.django_db
def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200

@pytest.mark.django_db
def test_services_page(client):
    response = client.get('/services/')
    assert response.status_code == 200

@pytest.mark.django_db
def test_clients_page(client):
    response = client.get('/clients/')
    assert response.status_code == 200

@pytest.mark.django_db
def test_contact_page_get(client):
    response = client.get('/contact/')
    assert response.status_code == 200

@pytest.mark.django_db
def test_contact_post(client):
    response = client.post('/contact/', {
        'name': 'Test User',
        'email': 'test@test.com',
        'message': 'Hello world',
    })
    assert response.status_code == 302

@pytest.mark.django_db
def test_service_model():
    s = Service.objects.create(title='Test Service', description='Test description')
    assert str(s) == 'Test Service'
