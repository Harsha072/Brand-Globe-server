import openai
import os
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Brand
from .serializers import BrandSerializer
from utils import generate_description
from dotenv import load_dotenv
# Set your OpenAI API key here
load_dotenv()
openai.api_key = os.getenv('OPENAI_KEY')

class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

    def create(self, request, *args, **kwargs):
        brand_name = request.data.get("name", "")
        
        # Call the new function to generate the description
        generated_description = generate_description(brand_name)

        if generated_description is None:
            return Response({"error": "Failed to generate description"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # Create the data dictionary
        data = {
            "name": brand_name,
            "description": generated_description,
            "logo": request.data.get("logo"),
        }

        # Validate and save the brand data
        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

   

    def update(self, request, pk=None, *args, **kwargs):
        brand = self.get_object()
        serializer = self.get_serializer(brand, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None, *args, **kwargs):
        brand = self.get_object()
        brand.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
