from tkinter import CASCADE
from django.db import models
from django.template.defaulttags import comment


class Master(models.Model):
    first_name = models.CharField(max_length=200, verbose_name="Имя")
    last_name = models.CharField(max_length=200, verbose_name="Фамилия")
    contact_info = models.TextField(verbose_name="Контактная информация")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    photo = models.ImageField(verbose_name="Фотография мастера")
    services = models.ManyToManyField("Service", related_name="masters")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Мастер"
        verbose_name_plural = "Мастера"


class Service(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Стоимость услуги"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"


class Visit(models.Model):
    STATUS_CHOICES = [
        (0, "Не подтверждена"),
        (1, "Подтверждена"),
        (2, "Отменена"),
        (3, "Выполнена"),
    ]

    name = models.CharField(max_length=200, verbose_name="Имя")
    phone = models.CharField(max_length=200, verbose_name="Телефон клиента")
    master = models.ForeignKey(
        "Master", on_delete=models.CASCADE, verbose_name="Выпадающий список мастеров"
    )
    services = models.ForeignKey(
        "Service",
        on_delete=models.CASCADE,
        verbose_name="выпадающий список услуг, которые предоставляет выбранный мастер",
    )
    comment = models.TextField(verbose_name="Комментарий")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    status = models.IntegerField(
        choices=STATUS_CHOICES, default=0, verbose_name="Статус"
    )
