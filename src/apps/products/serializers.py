from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from apps.products.models import Product


class ProductMaterialsSerializer(serializers.Serializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    quantity = serializers.IntegerField()

    def validate(self, attrs):
        """
        This method does very complex equations and returns the result
        """
        attrs = super().validate(attrs)
        product = attrs.get('product')
        quantity = attrs.get('quantity')
        material_warehouses = self.context['material_warehouses']
        material_products = product.materials.all()
        product_materials = []
        necessary_materials = {}

        for material_product in material_products:
            necessary_materials[material_product.material.name] = quantity * material_product.quantity

        for key, value in necessary_materials.copy().items():
            if key in material_warehouses:
                for material_warehouse in material_warehouses[key]:
                    if value == 0: break
                    if material_warehouse[2] == 0:continue
                    
                    if material_warehouse[2] >= value:
                        product_materials.append(
                            {
                            'warehouse': material_warehouse[0],
                            'material': key,
                            'quantity': value,
                            'price': material_warehouse[1],
                            }
                        )
                        necessary_materials[key] = 0
                        warehouse_index = material_warehouses[key].index(material_warehouse)
                        material_warehouses[key][warehouse_index][2] = material_warehouse[2] - value
                        break
                    else:
                        value -= material_warehouse[2]
                        product_materials.append(
                            {
                            'warehouse': material_warehouse[0],
                            'material': key,
                            'quantity': material_warehouse[2],
                            'price': material_warehouse[1],
                            }
                        )
                        necessary_materials[key] = value
                        warehouse_index = material_warehouses[key].index(material_warehouse)
                        material_warehouses[key][warehouse_index][2] = 0
                if necessary_materials[key] > 0:
                    product_materials.append(
                            {
                            'warehouse': None,
                            'material': key,
                            'quantity': necessary_materials[key],
                            'price': None,
                            }
                        )
                    

            else:
                product_materials.append(
                            {
                            'warehouse': None,
                            'material': key,
                            'quantity': necessary_materials[key],
                            'price': None,
                            }
                        )

        data = {
            'product_name':product.name,
            'product_quantity':quantity,
            'product_materials':product_materials    
            }

        self.context['material_warehouses'] = material_warehouses

        return data