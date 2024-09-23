from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from apps.products.serializers import ProductMaterialsSerializer
from apps.warehouse.models import Warehouse


class ProductMaterialsAPIView(GenericAPIView):
    """
    This view is will accept post requests
    """
    queryset = []

    serializer_class = ProductMaterialsSerializer

    def post(self, request, *args, **kwargs):
        warehouses = Warehouse.objects.all()

        material_warehouses = {}

        for warehouse in warehouses:
            if not warehouse.material.name in material_warehouses:
                material_warehouses[warehouse.material.name] = []
            material_warehouses[warehouse.material.name].append([warehouse.id, float(warehouse.price), int(warehouse.remainder)])
        
        serializer = self.get_serializer(data=request.data, many=True, context={'material_warehouses': material_warehouses})
        serializer.is_valid(raise_exception=True)
        result = {'result':serializer.validated_data}
        return Response(result, status=200)