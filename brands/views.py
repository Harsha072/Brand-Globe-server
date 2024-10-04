from django.shortcuts import render
from rest_framework import viewsets, status
from requests import Response
from rest_framework import viewsets
from .models import Brand
from .serializers import BrandSerializer

class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

     # Create a new brand
    from rest_framework.response import Response  # Correct import

    class BrandViewSet(viewsets.ModelViewSet):
        queryset = Brand.objects.all()
        serializer_class = BrandSerializer

        # Create a new brand
        def create(self, request, *args, **kwargs):
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Update a brand
        def update(self, request, pk=None, *args, **kwargs):
            brand = self.get_object()
            serializer = self.get_serializer(brand, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Delete a brand
        def destroy(self, request, pk=None, *args, **kwargs):
            brand = self.get_object()
            brand.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

    