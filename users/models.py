from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    """Модель пользователя"""

    username = None
    email = models.EmailField(
        unique=True, verbose_name="Email", help_text="Введите Вашу почту"
    )
    first_name = models.CharField(
        max_length=50, verbose_name="Имя", help_text="Введите имя"
    )
    last_name = models.CharField(
        max_length=50, verbose_name="Фамилия", help_text="Введите фамилию"
    )
    phone = PhoneNumberField(
        verbose_name="Номер телефона", help_text="Укажите Ваш телефон"
    )
    date_of_birth = models.DateField(
        verbose_name="Дата рождения", help_text="Введите дату рождения"
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.last_name} {self.first_name[:1]}. - {self.email}"

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
