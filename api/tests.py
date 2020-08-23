import pytest
import os
import uuid
from django.urls import reverse
from knox.models import AuthToken
from rest_framework.authtoken.models import Token

@pytest.fixture
def api_client():
    from rest_framework.test import APIClient
    return APIClient()


@pytest.fixture
def test_password():
   return 'strong-test-pass'


@pytest.fixture
def create_user(db, django_user_model, test_password):
    def make_user(**kwargs):
        kwargs['password'] = test_password
        if 'email' not in kwargs:
           kwargs['email'] = "test@newsletterapptest.com"
        return django_user_model.objects.create_user(**kwargs)
    return make_user()

@pytest.fixture
def api_client_with_credentials(db, create_user, api_client):
    user = create_user
    api_client.force_authenticate(user=user)
    yield api_client
    api_client.force_authenticate(user=None)


@pytest.mark.django_db
def test_login_request(api_client, create_user, test_password):
    url = reverse('login')
    user = create_user
    post_data = {
        "email": user.email,
        "password": test_password
    }
    response = api_client.post(path=url, data=post_data)
    assert response.status_code == 200


def test_send_mail_request(api_client_with_credentials):
    url = reverse('email')
    file_path = "test.html"
    f = open(file_path, "w")
    f.write("Test Mail")
    f.close()
    f = open(file_path, "r")
    post_data = {
        "subject": "test-subject",
        "content": f,
        "recipients": ["shashank16jaitly@gmail.com", "shashank16vasu@gmail.com"]
    }
    response = api_client_with_credentials.post(path=url, data=post_data)
    if os.path.exists(file_path):
        os.remove(file_path)
    assert response.status_code == 200
    
    
