from django.contrib import admin
from .models import Spirit,Order




@admin.register(Spirit)
class SpiritAdmin(admin.ModelAdmin):
    list_display = ("name", "country", "capacity", "reserved")


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("spirit", "quantity")