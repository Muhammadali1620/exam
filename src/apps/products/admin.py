from django.contrib import admin
from apps.products.models import Product, ProductMaterials


class InlineProductMaterials(admin.TabularInline):
    model = ProductMaterials
    

@admin.register(ProductMaterials)
class ProductMaterialAdmin(admin.ModelAdmin):
    list_display = ('id', 'quantity',)
    list_display_links = list_display


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'code',)
    list_display_links = list_display
    inlines = [InlineProductMaterials]