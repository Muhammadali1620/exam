from django.db import models
from django.core.validators import MinValueValidator


class Warehouse(models.Model):
    material = models.ForeignKey('materials.Material', on_delete=models.PROTECT, related_name='warehouses')
    remainder = models.PositiveSmallIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])

    def __str__(self):
        return str(self.remainder)