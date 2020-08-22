import pytest
from django.urls import reverse
from knox.models import AuthToken

@pytest.fixture
def api_client():
    from rest_framework.test import APIClient
    return APIClient

@pytest.fixture
def api_client_with_credentials(db, create_user, api_client):
    user = create_user()
    api_client.force_authenticate(user = user)
    yield api_client
    api_client.force_authenticate(user=NONE)


@pytest.mark.django_db
def test_unauthorized_request(api_client):
   url = reverse('login')
   response = api_client.get(url)
   assert response.status_code == 401


@pytest.fixture
def get_or_create_token(db, create_user):
   user = create_user()
   token = AuthToken.objects.create(user)[1] 
   return token


@pytest.mark.django_db
def test_unauthorized_request(api_client, get_or_create_token):
   url = reverse('login')
   token = get_or_create_token()
   api_client.credentials(AUTHORIZATION='Token ' + token)
   response = api_client.get(url)
   assert response.status_code == 200


@pytest.mark.django_db
def test_authorized_request(api_client_with_credentials):
   url = reverse('logout')
   response = api_client_with_credentials.get(url)
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
        "recipients": ["shashank.16jaitly@gmail.com", "shashank16vasu@gmail.com"]
    }
    response = api_client_with_credentials.post(url, data=post_data)
    assert response.status_code == 200
    if os.path.exists(fpath):
        return os.remove(fpath)
