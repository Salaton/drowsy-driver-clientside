import pytest
from django.test import Client
from django.urls import reverse


def test_home_view():
    """ Test the home page view"""
    client = Client()
    url = reverse("home")
    response = client.get(url)

    assert response.status_code == 200


def test_login_view():
    """Test the login view"""
    client = Client()
    url = reverse("login")
    response = client.get(url)

    assert response.status_code == 200


def test_signup_view():
    """Test the signup view"""
    client = Client()
    url = reverse("signup")
    response = client.get(url)

    assert response.status_code == 200


"""pytest-django provides both an unauthenticated client
and a logged-in admin_client as fixtures
Using admin_client because you just want to test the
redirect as easily as possible, without having to log in manually
"""


def test_statistics_view(admin_client):
    """Test the statistics view"""
    client = Client()
    url = reverse("stats")
    response = admin_client.get(url, follow=True)

    assert response.status_code == 200


def test_profile_view(admin_client):
    """Test the profile view"""
    client = Client()
    url = reverse("profile")
    response = admin_client.get(url, follow=True)

    assert response.status_code == 200
