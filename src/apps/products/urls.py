from django.urls import path

from apps.products.views import ProductMaterialsAPIView


urlpatterns = [
    path('materials/', ProductMaterialsAPIView.as_view(), name='product_materials')
]
