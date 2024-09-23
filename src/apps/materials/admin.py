from django.contrib import admin
from apps.materials.models import Material


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug',)
    list_display_links = list_display
    prepopulated_fields = {'slug': ('name',)}