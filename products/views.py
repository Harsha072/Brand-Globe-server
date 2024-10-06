from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from utils import generate_description

from brands.models import Brand
from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def create(self, request, *args, **kwargs):
        brand_id = request.data.get('brand')
        brand_name = request.data.get('name')

        if not brand_id:
            return Response({"error": "Brand ID is required"}, status=status.HTTP_400_BAD_REQUEST)

        # Use get_object_or_404 to simplify brand lookup
        brand = get_object_or_404(Brand, id=brand_id)

        # Generate the product description
        generated_description = generate_description(brand_name)

        if generated_description is None:
            return Response({"error": "Failed to generate description"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # You don't need to redefine the data here, just use request.data
        request.data['description'] = generated_description

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
