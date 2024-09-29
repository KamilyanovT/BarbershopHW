from tkinter import CASCADE
from django.db import models
from django.template.defaulttags import comment


class Master(models.Model):
    first_name = models.CharField(max_length=200, verbose_name="Имя")
    last_name = models.CharField(max_length=200, verbose_name="Фамилия")
    contact_info = models.TextField(verbose_name="Контактная информация")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    photo = models.ImageField(verbose_name="Фотография мастера")
    services = models.ManyToManyField(
        "Service", related_name="masters", verbose_name="Услуги"
    )

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
    name = models.CharField(max_length=255, verbose_name="Имя")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    master = models.ForeignKey(
        "Master", on_delete=models.CASCADE, verbose_name="Мастер"
    )
    services = models.ManyToManyField("Service", related_name="visit", verbose_name="Услуги")

    def __str__(self):
        return f"{self.name} - {self.phone}"

    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"
