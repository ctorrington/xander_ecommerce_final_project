"""Serializers for product app."""

from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    """Serializer for Product model."""
    
    class Meta:
        model = Product
        # fields = ('id', 'name', 'price', 'description', 'image', 'category')
        fields = '__all__'