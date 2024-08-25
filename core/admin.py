from django.contrib import admin
from .models import Visit, Master, Service


@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "created_at", "status")
    list_filter = ("status", "created_at")
    search_fields = ("name", "phone", "comment")


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
