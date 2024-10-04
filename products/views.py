from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from brands.models import Brand
from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def create(self, request, *args, **kwargs):
        brand_id = request.data.get('brand')
        try:
            brand = Brand.objects.get(id=brand_id)
            if brand_id == brand.id:
                print(f"Brand ID matched: {brand_id}")
            else:
                print(f"Brand ID not matching: request ID {brand_id}, database ID {brand.id}")
        except Brand.DoesNotExist:
            return Response({"error": "Brand not found"}, status=status.HTTP_400_BAD_REQUEST)
        
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        # Update a product
        partial = kwargs.pop('partial', False)
        product = self.get_object()
        serializer = self.get_serializer(product, data=request.data, partial=partial)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        # Delete a product
        product = self.get_object()
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
