import factory
from driver_stats.models import Stats
from users.models import DrowsyDriverUser


class UserFactory(factory.DjangoModelFactory):
    """
    Define user factory..
    """

    class Meta:
        model = DrowsyDriverUser


class StatsFactory(factory.DjangoModelFactory):
    """
    Define Stats Factory
    """

    class Meta:
        model = Stats

    user = factory.SubFactory(UserFactory)

