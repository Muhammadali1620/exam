from django.db import models
from django.core.validators import MinValueValidator


class Product(models.Model):
    name= models.CharField(max_length=100)
    code = models.SlugField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class ProductMaterials(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='materials')
    material = models.ForeignKey('materials.Material', on_delete=models.PROTECT, related_name='products')
    quantity = models.FloatField(default=0, validators=[MinValueValidator(0)])

    def __str__(self):
        return str(self.quantity)