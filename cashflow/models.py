from django.db import models
from django.utils import timezone

NULLABLE = {"null": True, "blank": True}


class Status(models.Model):
    """Модель статуса денежного потока."""

    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="Статус движения денежных средств",
        help_text="Введите статус",
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Статус"
        verbose_name_plural = "Статусы"


class OperationType(models.Model):
    """Модель тип операции."""

    name = models.CharField(
        max_length=50,
        verbose_name="Тип операции",
        unique=True,
        help_text="Введите тип операции",
    )

    def __str__(self):
        return f"Тип операции - {self.name}"

    class Meta:
        verbose_name = "Тип операции"
        verbose_name_plural = "Типы операций"


class Category(models.Model):
    """Модель категории операции."""

    name = models.CharField(
        max_length=100,
        verbose_name="Категория",
        help_text="Введите название категории",
        unique=True,
    )

    def __str__(self):
        return f"Категория - {self.name}"

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Subcategory(models.Model):
    """Модель подкатегории."""

    name = models.CharField(
        max_length=100,
        verbose_name="Подкатегория",
        help_text="Введите подкатегорию",
        unique=True,
    )
    category = models.ForeignKey(
        Category,
        verbose_name="Категория",
        help_text="Выберите категорию или введи вручную",
        on_delete=models.CASCADE,
        related_name="subcategory",
    )

    def __str__(self):
        return f"Подкатегория - {self.name}"

    class Meta:
        verbose_name = "Подкатегория"
        verbose_name_plural = "Подкатегории"


class CashFlow(models.Model):
    """Модель денежного потока."""

    created_at = models.DateField(
        verbose_name="Дата создания записи", default=timezone.now
    )

    status = models.ForeignKey(
        Status,
        verbose_name="Статус",
        on_delete=models.SET_NULL,
        null=True,
        help_text="Выберите статус операции",
    )
    operation_type = models.ForeignKey(
        OperationType,
        verbose_name="Тип операции",
        on_delete=models.SET_NULL,
        null=True,
        help_text="Выберите тип операции",
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        related_name="cashflows",
        verbose_name="Категория",
        help_text="Выберите категорию или введите вручную",
    )

    subcategory = models.ForeignKey(
        Subcategory,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Подкатегория",
        help_text="Выберите подкатегорию или введите вручную",
    )

    sum = models.DecimalField(
        max_digits=15, decimal_places=2, default=0.00, verbose_name="Сумма операции"
    )
    comment = models.TextField(
        verbose_name="Комментарий", help_text="Введите комментарий", **NULLABLE
    )

    def __str__(self):
        return f"{self.operation_type} {self.created_at} на сумму {self.sum}"

    class Meta:
        verbose_name = "Денежный поток"
        verbose_name_plural = "Денежные потоки"
