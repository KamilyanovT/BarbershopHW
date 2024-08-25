from django.contrib import admin
from .models import Visit, Master, Service


@admin.register(Visit)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("name", "master", "service")
    list_filter = ("name", "service")
    search_fields = ("name", "service")


@admin.register(Master)
class MasterAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "phone")
    search_fields = ("first_name", "last_name", "phone")
    list_filter = ("services",)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "price",
    )
    search_fields = ("name", "description")
