from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        """Команда для создания суперпользователя."""
        user = User.objects.create(
            email="admin@example.com",
            first_name="Admin",
            last_name="Adminov",
            phone="+7-900-800-00-01",
            date_of_birth="1996-07-19",
            is_staff=True,
            is_superuser=True,
            is_active=True,
        )

        user.set_password("pass")
        user.save()
