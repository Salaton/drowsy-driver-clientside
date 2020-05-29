import freezegun
import pytest
from .factories import UserFactory, StatsFactory
from datetime import datetime, timedelta


@pytest.mark.django_db
def test_user_model():
    """
    Test user model
    """
    # Create a user model instance
    user = UserFactory(
        first_name="Chelsea",
        last_name="Tuitoek",
        username="Tuchi",
        email="chelsea@gmail.com",
        car_registration_number="kca 234r",
        next_of_kin_name="Emmanuel Marin",
        next_of_kin_number="+254719158559",
        # password="chelsea-254",
    )

    assert user.first_name == "Chelsea"
    assert user.last_name == "Tuitoek"
    assert user.username == "Tuchi"
    assert user.email == "chelsea@gmail.com"
    assert user.car_registration_number == "kca 234r"
    assert user.next_of_kin_name == "Emmanuel Marin"
    assert user.next_of_kin_number == "+254719158559"


@pytest.mark.django_db
# @freezegun.freeze_time("2020-05-15")
def test_stats_model():
    """
    Test stats model
    """
    # Create user and stats model instance
    user = UserFactory(first_name="Chelsea")
    stats = StatsFactory(user=user, eye_aspect_ratio=2.5)

    assert stats.user == user
    assert stats.user.first_name == "Chelsea"
    assert stats.eye_aspect_ratio == 2.5
    # assert stats.time_alarm_raised == datetime.now()
