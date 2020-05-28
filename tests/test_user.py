import pytest
from django.urls import reverse
from django.test import Client

from users.models import DrowsyDriverUser


@pytest.mark.django_db
def test_user_create():
    client = Client()
    user = DrowsyDriverUser.objects.create(
        first_name="Chelsea",
        last_name="Tuitoek",
        username="Tuchi",
        email="chelsea@gmail.com",
        car_registration_number="kca 234r",
        next_of_kin_name="Emmanuel Marin",
        next_of_kin_number="0719158559",
        password="chelsea-254",
        # password_confirmation="chelsea-254",
    )
    url = reverse("signup")
    response = client.get(url)
    assert response.status_code == 200

    assert DrowsyDriverUser.objects.count() == 1
