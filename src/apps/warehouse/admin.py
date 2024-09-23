from django.contrib import admin
from apps.warehouse.models import Warehouse


@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    list_display = ('id', 'remainder', 'price',)
    list_display_links = list_display