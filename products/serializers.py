from rest_framework import serializers
from brands.models import Brand
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    brand = serializers.PrimaryKeyRelatedField(queryset=Brand.objects.all())  # Handle brand as input

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'category', 'price', 'image', 'brand']