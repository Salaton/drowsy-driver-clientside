from django.core.management.base import BaseCommand

# from users.models import DrowsyDetail


from utilities.video import vid


class Command(BaseCommand):
    """Command class."""

    help = "We are watching you"

    def add_arguments(self, parser):
        parser.add_argument("user", nargs="+", type=str)

    def handle(self, *args, **options):
        """Anything below is run as a custom command."""
        vid(options["user"])
